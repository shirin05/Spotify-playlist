import spotipy
import base64
import requests
import json
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint
cid = "81f75550c9534a07a56a8d1f6838996a"
secret = "3be13743b0a04cdfadb68e864a40a989"
scope = "user-library-read playlist-modify-public playlist-modify"
user_id = "23680fcf4d0c4831"
user_id = "rijulmahajan"


# python3 real_api.py 6fd934e6446e4e58

oauth = spotipy.SpotifyOAuth(client_id=cid,client_secret= secret, redirect_uri="http://google.com/", scope=scope)
token = oauth.get_access_token()
# pprint(token['access_token'])
sp = spotipy.Spotify(auth=token['access_token'])

# get user details 
user = sp.current_user()
display_name = user['display_name']

# pprint(sp.me())
pprint(sp.user(user_id))


# class that will hold helper functions for spotify API
class SpotifyHelperBase():
     def __init__(self, spotipy_object):
          self.sp = spotipy_object

     def get_user_id(self):
          return self.sp.current_user()['id']
     
     def get_user_name(self):
          return self.sp.current_user()['display_name']



# class that will hold custom functions that are specialised to the libary of songs
# self refers to functions or variables in the same class 
# init is the initilaisation function 
# when an object is made, it defines the needed parameters and variables for the rest of the class
class SpotifyHelperLibrary(SpotifyHelperBase):
     def __init__(self, spotipy_object):
          super().__init__(spotipy_object)
          # print all the methods of the spotipy object
     
     # PLAYLIST FUNCTIONS 
     def get_user_playlists(self):
          return self.sp.user_playlists(self.get_user_id())

     def display_user_playlists(self):
          playlists = self.get_user_playlists()
          for playlist in playlists['items']:
               print("Playlist number: {}".format(playlists['items'].index(playlist) + 1))
               print("Playlist Name: " + playlist['name'])
               print("Playlist ID: " + playlist['id'])
               print("Playlist Length: " + str(playlist['tracks']['total']))
               print("\n")


     def display_playlist_tracks(self, user_id, playlist_id):
          # get the tracks in the playlist
          playlist_tracks = self.sp.user_playlist_tracks(user_id, playlist_id)
          # get the tracks
          tracks = playlist_tracks['items']
          # print the tracks
          for track in tracks:
               print("Track Number: {}".format(playlist_tracks['items'].index(track) + 1))
               print("Track Name: " + track['track']['name'])
               print("Track Artist: " + track['track']['artists'][0]['name'])
               print("Track Album: " + track['track']['album']['name'])
               print("\n")

     def get_user_library(self):
          return self.sp.current_user_saved_tracks()

     def display_user_library(self):
          library = self.get_user_library()
          for track in library['items']:
               print("Track Number: {}".format(library['items'].index(track) + 1))
               print("Track Name: " + track['track']['name'])
               print("Track Artist: " + track['track']['artists'][0]['name'])
               print("Track Album: " + track['track']['album']['name'])
               print("\n")

     # function to save all uri of the library to a queue
     def get_library_uris(self):
          library = self.get_user_library()
          uris = []
          for track in library['items']:
               uris.append(track['track']['uri'])
          return uris

     # function to get audio features for all tracks in user library
     def get_library_features(self, library_uris):
          # if statement to check in case there are no uris 
          if library_uris == []:
               print("Your library has no tracks.")
               return library_uris
          
          # created a list with all the features
          library_features = []

          # if statment to run when the total tracks are less than or equal to 100
          if len(library_uris) <= 100:
               # appends features list 
               library_features += self.sp.audio_features(library_uris)
               return library_features
	
	     # find quotient
          quotient = len(library_uris)//100
          
          # if statment to get uris of the tracks that are in a group of less than a 100
          # for example, if there are 250 tracks, this will run on 50 tracks
          # it finds the number of tracks to run on by finding the remainder
          if len(library_uris) % 100 != 0:
               product = quotient * 100
               library_features += self.sp.audio_features(library_uris[product:len(library_uris)])

          # continuing with example now we have 250 - 50 = 200 tracks
          # in increments of 100, the 200 tracks will be passed as parameters
          for i in range(0, product, 100):
               library_features += self.sp.audio_features(library_uris[i:i+99])
          
          return library_features


     # function to make a new playlist and add given tracks to it 
     def make_playlist(self, playlist_name, playlist_description, playlist_tracks):
          # create a new playlist
          new = self.create_playlist(token, self.get_user_id(), playlist_name)
          # get the playlist id
          playlist_id = new['id']
          # add tracks to the playlist
          self.add_to_playlist(token['access_token'], playlist_id, playlist_tracks)
          # return the playlist id
          return playlist_id
     
          # method to create a playlist
     def create_playlist(token, user_id, playlist_name):
          create_url = "https://api.spotify.com/v1/users/{}/playlists".format(user_id)
          create_header = {
               "Authorization": "Bearer " + token
          }
          create_data = {
               "name": playlist_name,
               "description": "Playlist created by a bot",
               "public": True
          }
          res = requests.post(create_url, headers = create_header, data = create_data)
          create_object = res.json()
          return create_object

     # function to add a list of songs to a playlist
     def add_to_playlist(token, my_playlist_id, track_list):
          add_url = "https://api.spotify.com/v1/playlists/{}/tracks".format(my_playlist_id)
          add_header = {
               "Authorization": "Bearer " + token
          }
          add_data = {
               "uris": track_list
          }
          res = requests.post(add_url, headers = add_header, data = add_data)
          add_object = res.json()
          return add_object

                

          

# # print all the functions of the library class
# pprint(dir(SpotifyHelperLibrary))

# hi = SpotifyHelperLibrary(sp)
# pprint(dir(hi))
# pprint(vars(hi))