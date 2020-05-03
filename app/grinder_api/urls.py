from django.urls import path,include,re_path
from rest_framework import routers
from grinder_api import views
from .serializers import UserViewSet, GroupViewSet, TrackViewSet, PlaylistViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'group', GroupViewSet)
router.register(r'track', TrackViewSet)
router.register(r'playlist', PlaylistViewSet)

urlpatterns = [
    path(r'', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api/', include(router.urls)),
    re_path(r'^login(?:\/)?$', views.Login.as_view()),
    re_path(r'^login/refresh(?:\/)?$', views.LoginRefresh.as_view()),
    path('login/register', views.Register.as_view()),
]
