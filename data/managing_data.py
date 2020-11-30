import pymongo
import json
from config import *

client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster0.mo20d.mongodb.net/Song?retryWrites=true&w=majority")
mydb = client[f"{database_name}"]
collection = mydb[f"{collection_name}"]


def get_data_from_api():

    import http.client

    conn = http.client.HTTPSConnection("deezerdevs-deezer.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "e4b887b616msh530806fb9091fc4p152779jsnd0d12a497314",
        'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com"
        }

    conn.request("GET", "/track/491446962", headers=headers)

    res = conn.getresponse()

    data = json.loads(res.read())
    collection.insert_many([data])

def get_number_of_albums():
    for num in collection.find({'name':"Post Malone"}):
        number_of_album = num['nb_album']
    return number_of_album

def get_number_of_fans():
    for num in collection.find({'name':"Post Malone"}):
        number_of_fans = num['nb_fan']
    return number_of_fans

def get_facebook():
    data = collection.find()
    facebook = data[12]['response']['artist']['facebook_name']
    return facebook

def get_twitter():
    data = collection.find()
    twitter = data[12]['response']['artist']['twitter_name']
    return twitter

def get_instagram():
    data = collection.find()
    instagram  = data[12]['response']['artist']['instagram_name']
    return instagram

def get_top_track():
    response = collection.find()
    data1 = list(response[13]['tracks'])[0:5]
    top_track = []
    for i in data1:
        top_track.append(i['title'])
    return top_track

def get_info_track_one():
    response = collection.find()
    data = response[14]
    release_date = data['release_date']
    available_countries_th = data['available_countries'][182]
    available_countries_us = data['available_countries'][194]
    return release_date, available_countries_th, available_countries_us


def get_info_track_two():
    response = collection.find()
    data = response[15]
    release_date = data['release_date']
    available_countries_th = data['available_countries'][182]
    available_countries_us = data['available_countries'][194]
    return release_date, available_countries_th, available_countries_us

def get_info_track_three():
    response = collection.find()
    data = response[16]
    release_date = data['release_date']
    available_countries_th = data['available_countries'][178]
    available_countries_us = data['available_countries'][190]    
    return release_date, available_countries_th, available_countries_us

def get_info_track_four():
    response = collection.find()
    data = response[17]
    release_date = data['release_date']
    available_countries_th = data['available_countries'][182]
    available_countries_us = data['available_countries'][194]    
    return release_date, available_countries_th, available_countries_us

def get_info_track_five():
    response = collection.find()
    data = response[18]
    release_date = data['release_date']
    available_countries_th = data['available_countries'][178]
    available_countries_us = data['available_countries'][190]    
    return release_date, available_countries_th, available_countries_us

# data = {
#     'id': '60693584-55ea-4897-949a-51be76ad3ff1',
#     'artist': 'Post Malone',
#     'number_of_albums': get_number_of_albums(),
#     'number_of_fans': get_number_of_fans(),
#     'contacts':[{
#         'facebook': get_facebook(),
#         'twitter' : get_twitter(),
#         'instagram' : get_instagram()
#     }],
#     'charts': [
#         {
#             '2020-09-26': 10,
#             '2020-10-03': 0,
#             '2020-10-10': 0,
#             '2020-10-17': 0,
#             '2020-10-24': 10 
#         }
#     ],
#     'top_tracks':[
#         {
#             'title': get_top_track()[0],
#             'release_date': one_release_date,
#             'available_countires': [{
#                 '0': three_available_countires_th,
#                 '1': three_available_countires_us 
#             }]
#         },
#         {
#             'title': get_top_track()[1],
#             'release_date': two_release_date,
#             'available_countires': [{
#                 '0': two_available_countires_th,
#                 '1': two_available_countires_us
#             }]
#         },
#         {
#             'title': get_top_track()[2],
#             'release_date': three_release_date,
#             'available_countires': [{
#                 '0': three_available_countires_th,
#                 '1': three_available_countires_us   
#                 }]     
#         },
#         {
#             'title': get_top_track()[3],
#             'release_date': four_release_date,
#             'available_countires': [{
#                 '0': three_available_countires_th,
#                 '1': three_available_countires_us 
#                 }]
#         },
#         {
#             'title': get_top_track()[4],
#             'release_date': five_release_date,
#             'available_countires': [{
#                 '0': three_available_countires_th,
#                 '1': three_available_countires_us 
#             }]
#         }
#     ]

# }