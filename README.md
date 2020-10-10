h4. Food Assistant Script

If you are having a heard time deciding where to eat; this script makes it a bit easier.
It gives you 5 cuisine options and gets you top 3 restaurants based on ratings from  the cuisine you select.
It then opens a yelp page for the restaurant so you can browse menu and order :)

Requires:
A file called api.key in directory of the script that contains the Yelp Fusion API key
The file simply contains the key and nothing else
For API key details refer: https://www.yelp.com/developers/documentation/v3/authentication

Python 3.8 Libraries used:
geocoder
json
requests
itertools
collections.OrderedDict
sys
webbrowser

Usage:

C:\Users\adity\Documents\food_assist_yelp>python foodAssister.py
what do you feel like eating?
Here are your options--
1.Ramen
2.Indian
3.Vegan
4.Mediterranean
5.Chinese

Enter No: 1
Top 3 restaurants of cuisine ramen:
1. Name: Ramen Mori, Rating: 5.0

2. Name: HiroNori Craft Ramen, Rating: 4.5

3. Name: Ramen One, Rating: 4.5

Enter restaurant choice
3

Site 3 --> Ramen One webpage will open on default webbrowser.
