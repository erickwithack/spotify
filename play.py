import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

scope = "playlist-modify-public"
username = "e39il2ffbg5s62j999fb23uer"

token = SpotifyOAuth(scope=scope, username=username)

spotifyObject = spotipy.Spotify(auth_manager=token)

#create a playlist
playlist_name = input("Enter playlist name: ")
playlist_description = input("Enter description: ")

spotifyObject.user_playlist_create(user=username, name=playlist_name, public=True, description=playlist_description)

user_input = input("Enter the song: ")
l = []

while (user_input!="quit"):
    results = spotifyObject.search(q=user_input)
    l.append(results['tracks']['items'][0]['uri'])
    user_input = input("Enter the song: ")

#create playlist
preplaylist = spotifyObject.user_playlists(user=username)
playlist = preplaylist['items'][0]['id']

#add songs
spotifyObject.user_playlist_add_tracks(user=username, playlist_id=playlist, tracks=l)