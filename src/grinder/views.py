from django.shortcuts import render, redirect

# Create your views here
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import requests
import os
import base64
import json
from urllib.parse import quote
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
User = get_user_model()

print('''"Real knowledge is to know the extent of one's ignorance."'''+'\n                       '+"~Confucius~")

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
    # "state": STATE,
    "show_dialog": SHOW_DIALOG_str,
    "client_id": CLIENT_ID
}

def CreateUser(request):
    # creates new user in db
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print("user = form.save()", user)
            user_name = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=user_name, password=raw_password)
            print("user = form.authenticate()", user)
            login(request, user)
            return redirect ('GetUser')
    else:
        form = CustomUserCreationForm()
    return render(request, 'sign_up.html', context={'form': form})


def GetUser(request):
    if request.method == 'POST':
        # gets user from db if valid and updates if needed access & refresh tokens
        # First we get username and password to auth spotify-grinder user
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        print(user_name, password)
        user = authenticate(username=user_name, password=password)
        if user is not None:
            # A backend authenticated the credentials
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                # Auth Step 1: Authorization
                url_args = "&".join(["{}={}".format(key, quote(val)) for key, val in auth_query_parameters.items()])
                auth_url = "{}/?{}".format(SPOTIFY_AUTH_URL, url_args)
                return redirect(auth_url)
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your spotify-grinder account is disabled.")
        else:
             # No backend authenticated the credentials
             return HttpResponse("This spotify-grinder account is not valid.")
    else:
        return render(request, 'sign_in.html', context={})

# Auth step 2: User login

# Auth step 3: Spotify redirects the User to auth

@login_required(login_url='sign_in/')
def auth(request):
    # Auth Step 4: Requests refresh and access tokens
    auth_token = request.GET.get('code')
    user.spRefresh()
    code_payload = {
        "grant_type": "authorization_code",
        "code": str(auth_token),
        "redirect_uri": REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }
    post_request = requests.post(SPOTIFY_TOKEN_URL, data=code_payload)

    # Auth Step 5: Tokens are Returned to Application
    response_data = json.loads(post_request.text)
    access_token = response_data["access_token"]
    refresh_token = response_data["refresh_token"]
    token_type = response_data["token_type"]
    expires_in = response_data["expires_in"]

    # Updating the user.access_token
    user = User.objects.get(username=request.user.username)
    
    # Update User tokens and expire date 
    user.access_token = access_token 
    user.refresh_token = refresh_token
    user.expires_in = expires_in

    # Auth Step 6: Use the access token to access Spotify API
    authorization_header = {"Authorization": "Bearer {}".format(access_token)}

    # Get profile data
    Current_users_profile_APIendpoint = "{}/me".format(SPOTIFY_API_URL)
    User_profile_APIendpoint = "{}/users/{}".format(SPOTIFY_API_URL, user.username)
    profile_response = requests.get(User_profile_APIendpoint, headers=authorization_header)
    profile_data = json.loads(profile_response.text)

    # top 100 tracks
    top50_Apiendpoint ="{}/top/tracks".format(Current_users_profile_APIendpoint)
    top50_response = requests.get(top50_Apiendpoint, headers=authorization_header)
    top50 = json.loads(top50_response.text)
    ids = ''
    for item in top50["items"]:
        x = item["id"]
        ids += x + ','
    top50_audiofeatures_APIendpoint = "{}/audio-features/?ids={}".format(SPOTIFY_API_URL, ids)
    top50_audiofeatures_response = requests.get(top50_audiofeatures_APIendpoint, headers=authorization_header)
    top50_audiofeatures = json.loads(top50_audiofeatures_response.text)
    # for item in top50["audio_features"]:
    #     x = item["id"]
    #     valence
    #     tempo
    #     speechiness
    #     popularity
    #     mode
    #     loudness
    #     liveness
    #     key
    #     instrumentalness
    #     energy
    #     danceability
    #     acousticness
    # recommendations_APIendpoint = "{}/recommendations?{}".format(SPOTIFY_API_URL, seed)
    # recommendations = requests.get(recommendations_APIendpoint , headers=authorization_header)


    user_urls = profile_data["external_urls"]
    user_sp_url = user_urls["spotify"]
    name = profile_data["display_name"]
    print(name, user_sp_url)

    # Get user playlist data
    playlist_api_endpoint = "{}/playlists".format(profile_data["href"])
    playlists_response = requests.get(playlist_api_endpoint, headers=authorization_header)
    playlist_data = json.loads(playlists_response.text)

    # create user output
    output = '''<blockquote class="blockquote">'''
    for item in playlist_data["items"]:
        playlist_names = item["name"]
        herfs = item["external_urls"]
        playlist_hrefs = herfs["spotify"]
        output +=  '''<kbd> <a href="'''+ playlist_hrefs +'''">'''+playlist_names+'''</a> </kbd> <br>'''
    output += "</blockquote>"

    return render(request, 'index.html', {'spuser':name,'spuser_url':user_sp_url, 'out':output})
