import spotipy
import time
from flask import Flask, request, url_for, session, redirect, jsonify
import requests
import helpers

app = Flask(__name__)

app.config['SPOTIFY_PROJ_COOKIE_NAME'] = 'Spotify Cookie'

# app.secret_key = client_secret


@app.route('/')
def home():
    return jsonify({'message': 'Hello, this application generates Spotify playlist links from Apple Music and Vice Versa, enjoy!'})

# @app.route('/')
# def playlist_link_info():


@app.route('/spotifyPlaylist')
def playlist_link():
    return helpers.return_playlist_link()

#call return 
