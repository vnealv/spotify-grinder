from django.contrib.auth.models import User, Group
from rest_framework import serializers,viewsets
from .models import grinderuser, Track


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = grinderuser
        fields = ['url', 'username', 'email', 'groups','spid']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class TrackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Track
        fields = ['id','spid','name','duration_ms','href','owner','stream_source']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint  allows users to be viewed or edited.
    """
    queryset = grinderuser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint  allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TrackViewSet(viewsets.ModelViewSet):
    """
    API endpoint  allows Tracks to be viewed or edited.
    """
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
