import configparser
from requests.models import InvalidURL
import spotipy as sp
from spotipy.client import Spotify
from spotipy.oauth2 import SpotifyOAuth
import subprocess
import time
import threading

config = configparser.RawConfigParser()
config.read('C://Users//ashish//AppData//Local//Programs//Python//Python39//Doc//smart mirror//config.ini')
Usarname = config['Spotify']['Username']
Client_ID = config['Spotify']['Client_ID']
Client_Secret = config['Spotify']['Client_Secret']
Device_Name = config['Spotify']['Device_Name']
redirecting_url = config['Spotify']['redirecting_url']
scope = config['Spotify']['scope']


authentor = SpotifyOAuth(
        client_id = Client_ID,
        client_secret = Client_Secret,
        redirect_uri = redirecting_url,
        scope = scope,
        username=Usarname)
spotify = sp.Spotify(auth_manager= authentor)

def Selecting_device():
    devices = spotify.devices()
    deviceID = None
    for d in devices['devices']:
        d['name'] = d['name'].replace('‘', '\'')
        if d['name'] == Device_Name:
            deviceID = d['id']
            return deviceID 
def Open_Spotifly():
    subprocess.call('C:/Users/ashish/AppData/Roaming/Spotify/Spotify.exe')

def player():
    playlist1 = 'My playlist #3'
    results = spotify.search(q= playlist1, limit = 20, type= 'playlist')
    songlist = threading.Thread(target=Open_Spotifly)
    songlist.start()
    print ("hi")
    time.sleep(7)
    deviceID = Selecting_device()
    if not results['playlists']['items']:
        raise KeyError
    track_uri = results['playlists']['items'][0]['uri']
    spotify.start_playback(device_id=deviceID, context_uri=track_uri)

