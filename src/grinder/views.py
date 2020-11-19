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
import datetime
from django.utils import timezone
from .SpotifyWrapper import Spotify

User = get_user_model()
sp = Spotify()

def Refresh(User):
    user.access_token , user.refresh_token, user.expires_in = sp.RefreshTokens(User.refresh_token)
    user.last_login = timezone.now()
    user.save(update_fields=['access_token', 'refresh_token', 'expires_in', 'last_login'])
    return User.access_token

def CreateUser(request):
    # creates new user in db
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_name = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=user_name, password=raw_password)
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
                user.last_login = timezone.now()
                user.save(update_fields=['last_login'])
                if user.refresh_token:
                    return redirect ( 'auth' )
                else:
                    return redirect(sp.getRedirectURL())
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your spotify-grinder account is disabled.")
        else:
             # No backend authenticated the credentials
             return HttpResponse("This spotify-grinder account is not valid.")
    else:
        return render(request, 'sign_in.html', context={})

@login_required(login_url='sign_in/')
def auth(request):
    user = User.objects.get(username=request.user.username)
    # Auth Step 4: Requests refresh and access tokens
    auth_token = request.GET.get('code')
    if auth_token:
        user.access_token , user.refresh_token, user.expires_in = sp.getTokens(auth_token)
        user.last_login = timezone.now()
        user.save(update_fields=['access_token', 'refresh_token', 'expires_in', 'last_login'])
        access_token = user.access_token
    else:
        access_token = Refresh(user)

    profile_data = sp.getProfile(user.access_token, user.username)

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


    user_sp_url = user_urls["spotify"]
    user_urls = profile_data["external_urls"]
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
