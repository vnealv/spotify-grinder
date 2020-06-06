from datetime import datetime, timedelta
from .models import grinderuser
import jwt
from django.conf import settings


def generate_tokens(user):

    if not (isinstance(user, grinderuser)):
        return None

    utc_now = datetime.utcnow()
    access_payload = {
        'iat': utc_now,
        'exp': utc_now + timedelta(minutes=60),
        'nbf': utc_now,
        'iss': "http://localhost:8000/grinder_api/login",  #replace with domain name after production
        'username': grinderuser.username,
        'email': grinderuser.email,
        'type': 'access'
    }

    access_token = jwt.encode(access_payload, settings.SECRET_KEY, algorithm='HS256')

    refresh_payload = {
        'iat': utc_now,
        'exp': utc_now + timedelta(days=2),
        'nbf': utc_now,
        'iss': "http://localhost:8000/grinder_api/login",  #replace with domain name after production
        'username': grinderuser.username,
        'type': 'refresh',
    }

    refresh_token = jwt.encode(refresh_payload, settings.SECRET_KEY, algorithm='HS256')

    return access_token, refresh_token
