import requests
import os
import base64
import json
import datetime
from urllib.parse import quote

class Spotify:
    #  Client Keys
    CLIENT_ID= os.environ.get("CLIENT_ID")
    CLIENT_SECRET= os.environ.get("CLIENT_SECRET")

    # Spotify URLS
    SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
    SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
    SPOTIFY_API_BASE_URL = "https://api.spotify.com"
    API_VERSION = "v1"
    SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)

    # Server-side Parameters
    CLIENT_SIDE_URL =  os.environ.get("client_side_url")
    PORT = os.environ.get("port")
    REDIRECT_URI = "{}:{}/callback/q".format(CLIENT_SIDE_URL, PORT)
    SCOPE = "playlist-modify-public playlist-modify-private user-top-read playlist-read-collaborative playlist-read-private"
    STATE = ""
    SHOW_DIALOG_bool = True
    SHOW_DIALOG_str = str(SHOW_DIALOG_bool).lower()
    auth_query_parameters = {
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPE,
        "state": STATE,
        "show_dialog": SHOW_DIALOG_str,
        "client_id": CLIENT_ID
    }

    def RefreshTokens(self, refresh_token):
        # Authorization is a base64 encoded string of client_id+client_secret
        encodedData = base64.b64encode(bytes(f"{self.CLIENT_ID}:{self.CLIENT_SECRET}", "ISO-8859-1")).decode("ascii")
        authorization_header_string = f"Basic {encodedData}"
        print (authorization_header_string)

        refresh_query_parameters = {
            "Authorization":str(authorization_header_string),
            "grant_type": str('authorization_code'),
            "refresh_token": refresh_token,
        }

        post_request = requests.post(self.SPOTIFY_TOKEN_URL, data=refresh_query_parameters)
        print('post_request:' + str(post_request))

        response_data = json.loads(post_request.text)
        print('response_data:'+str(response_data))

        access_token = response_data["access_token"]
        refresh_token = response_data["refresh_token"]
        token_type = response_data["token_type"]
        expires_in = response_data["expires_in"]

        return access_token, refresh_token, expires_in

    def getRedirectURL(self):
        # Auth Step 1: Authorization
        url_args = "&".join(["{}={}".format(key, quote(val)) for key, val in self.auth_query_parameters.items()])
        auth_url = "{}/?{}".format(self.SPOTIFY_AUTH_URL, url_args)
        return auth_url

        # Auth step 2: User login

        # Auth step 3: Spotify redirects the User to auth

    def getTokens(self, auth_token):
        # Auth Step 4: Requests refresh and access tokens
        code_payload = {
            "grant_type": "authorization_code",
            "code": str(auth_token),
            "redirect_uri": self.REDIRECT_URI,
            "client_id": self.CLIENT_ID,
            "client_secret": self.CLIENT_SECRET,
        }
        post_request = requests.post(self.SPOTIFY_TOKEN_URL, data=code_payload)
        # Auth Step 5: Tokens are Returned to Application
        response_data = json.loads(post_request.text)
        access_token = response_data["access_token"]
        refresh_token = response_data["refresh_token"]
        token_type = response_data["token_type"]
        expires_in = response_data["expires_in"]
        return access_token, refresh_token, expires_in

    def getProfile(self, access_token, username):
        # Auth Step 6 setting Authorization header
        authorization_header = {"Authorization": "Bearer {}".format(access_token)}
        # Get profile data
        User_profile_APIendpoint = "{}/users/{}".format(SPOTIFY_API_URL, username)
        profile_response = requests.get(User_profile_APIendpoint, headers=authorization_header)
        profile_data = json.loads(profile_response.text)
        return profile_data
