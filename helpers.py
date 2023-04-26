import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import re
from dotenv import load_dotenv
from urllib.error import HTTPError

load_dotenv()

PLAYLIST = 'https://open.spotify.com/playlist/37i9dQZF1DZ06evO2EsWju?si=8498eea2d6bd4c40'

# get a bearer token
def get_token():
    spotify = SpotifyClientCredentials(client_id=os.getenv('client_id'),
                                    client_secret=os.getenv('client_secret'))
    access_token_info = spotify.get_access_token()
    return access_token_info["access_token"]

#validates the spotify link 
def validate_spotify_link(link):
    pattern = r'https:\/\/open\.spotify\.com\/playlist\/[a-zA-Z0-9]+(\?si=[a-zA-Z0-9]+)?$'
    return bool(re.match(pattern, link))

def get_playlist_id(link):
    # this link is for a rock and roll playlist
    if validate_spotify_link(link):
        sp = spotipy.Spotify(get_token())
        link_split = link.split('/')
        playlist_id_link = link_split[-1].split('?')
        playlist_id = playlist_id_link[0]
        try:
            sp.playlist(playlist_id)
            return str(playlist_id)
        except spotipy.exceptions.SpotifyException:
            print(f"Invalid playlist ID with link: {link}, retry")
        except HTTPError :
            print(f"Invalid playlist ID with link: {link}, retry")
        except requests.ConnectionError:
            print(f"Invalid playlist ID with link: {link}, retry")
    return f"Invalid Playlist Link {link}, retry"


def get_playlist_items():
    # access_token = get_token()
    sp = spotipy.Spotify(get_token())
    # playlist id will be parsed into this function and that will be used in the playlist items
    items = sp.playlist(get_playlist_id(PLAYLIST))
    song_by_artist = []
    tracks = items['tracks']['items']
    
    for track_info in tracks:
        song_name = track_info['track']['name']
        artist_name = track_info['track']['artists'][0]['name']
        song_by_artist.append(f"{song_name} by {artist_name}")

    return song_by_artist

def get_playlist_name():
    #access_token = get_token()
    sp = spotipy.Spotify(auth=get_token())
    # playlist id will be parsed into this function and that will be used in the playlist items
    items = sp.playlist(get_playlist_id(PLAYLIST))
    return items['name']


def get_songs():
    '''
    does a search query from spotify for every song and adds it into an array and will be called 
    by the playlist maker to put the songs in a playlist
    '''
    pass



def return_playlist_link():
    '''
    return the playlist link to the user 
    '''
    pass










# print('This is the client key:' + json.dumps(get_token()))
print(get_playlist_items())
# print(get_playlist_items())
