from __future__ import print_function    # (at top of module)
import json
import time
import sys
import configparser
import spotipy
import spotipy.util as util
import spotipy.oauth2 as oauth2
from spotipy.oauth2 import SpotifyClientCredentials
import pprint

# using configparser to import [SPOTIFY] CLIENT_ID and CLIENT_SECRET from a file called config.cfg
config = configparser.ConfigParser()
config.read('/usr/src/app/grinder_api/config.cfg')
client_id = config.get('SPOTIFY', 'CLIENT_ID')
client_secret = config.get('SPOTIFY', 'CLIENT_SECRET')

auth = oauth2.SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)

#creating a sp object from spotipy class
sp = spotipy.Spotify(client_credentials_manager = auth)
sp.trace = False
token = auth.get_access_token(as_dict=True)

print('Hi grinder_user this is your client spotify token:', token)
print('-----------------------------------------------')
pp = pprint.PrettyPrinter(indent=4)
#pp.pprint()
tid = 'spotify:track:1ntxpzIUbSsizvuAy6lTYY'

start = time.time()
analysis = sp.audio_analysis(tid)
delta = time.time() - start
print(json.dumps(analysis, indent=4))
print("analysis retrieved in %.2f seconds" % (delta,))
