# App to assist with food queries
# Sorts food based on Mood /Cuisine you want to eat.
# Class to create a request object to query Yelp
# Queries include latitiude, longitude and a  search term for cuisine
# Author: Aditya Gawade

import geocoder
import json
import requests
import itertools
from collections import OrderedDict
import sys
import webbrowser

# File for referencing API key
api_file = "api.key"


class YelpRequest(object):
    api_key = str(open(api_file,"r").readlines()[0]).rstrip()
    yelp_url = "https://api.yelp.com/v3"
    token = "Bearer {}".format(api_key)

    def __init__(self, request,latitude, longitude, cuisine):
        self.request = request
        self.latitude = latitude
        self.longitude = longitude
        self.cuisine = cuisine

    def sendSearchGet(self,request, latitude, longitude, cuisine):
        http_request = "{0}/{1}?term={2}&latitude={3}&longitude={4}".format(self.yelp_url,
        self.request,self.cuisine,self.latitude, self.longitude)

        headers = {
        "Authorization": self.token,
        "Content-Type": "application/json"
        }

        r = requests.get(http_request, headers=headers)
        return r.json()


# switch case to pick a cuisine keyword for the request
def cuisineSwitch(choice):
    switcher = {
    1: "ramen",
    2: "indian",
    3: "vegan",
    4: "mediterranean",
    5: "chinese"
    }
    return switcher.get(choice, "Cuisine not in list")

# Display list of available cuisine options
def decideCuisine():
    print("what do you feel like eating?")
    print("Here are your options--")
    print("1.Ramen\n2.Indian\n3.Vegan\n4.Mediterranean\n5.Chinese\n")
    choice = int(input("Enter No: "))
    cuisine = cuisineSwitch(choice)
    return cuisine

# Returns dictionary with name and rating
# Sorted with high rating values at top
def getRestaurantList(bussData):
    nameRating = {}
    for buss in bussData['businesses']:
        nameRating[buss['name']] = buss['rating']
    ratedDict = OrderedDict(sorted(nameRating.items(), key=lambda x: x[1], reverse=True))
    return ratedDict

# Get highest rated 3 restaurants from the list
def getTopThree(ratedDict):
    if len(ratedDict.keys()) >= 3:
        topThree = itertools.islice(ratedDict.items(), 0, 3)
        return topThree
    else:
        return ratedDict

# Open restaurant on yelp site using webbrowser library
def getRestaurantSite(bussData, name):
    site = None
    for buss in bussData['businesses']:
        if buss['name'] == name:
            site = buss['url']
    return site

# Get restaurnt choice based on cuisine
def getRestaurantChoice(restDict, bussData, cuisine):
    print("Top 3 restaurants of cuisine {}:".format(cuisine))
    count = 1
    choiceMap = {}
    for key, value in restDict:
        print("{0}. Name: {1}, Rating: {2}\n".format(count, key, value))
        choiceMap[count] = key
        count = count + 1

    resChoice = int(input("Enter restaurant choice\n"))

    if resChoice not in choiceMap.keys():
        print("Enter Valid restaurant choice; please start again")
        sys.exit(0)

    site = getRestaurantSite(bussData, choiceMap[resChoice])
    webbrowser.open(site)


if __name__=="__main__":
    # Get latitude and longitude from geocoder library
    g = geocoder.ip('me')
    latitude = g.latlng[0]
    longitude = g.latlng[1]

    # endpoint for querying businesses
    request = "businesses/search"

    # cuisine acts as a filter for search
    cuisine = decideCuisine()
    if cuisine != "Cuisine not in list":
        yelp_req = YelpRequest(request, latitude, longitude, cuisine)
        bussData = yelp_req.sendSearchGet(request, latitude, longitude, cuisine)
        ratedDict = getRestaurantList(bussData)
        topDict = getTopThree(ratedDict)
        getRestaurantChoice(topDict, bussData, cuisine)
    else:
        print("Please enter cuisine choice from list")
        sys.exit(0)
