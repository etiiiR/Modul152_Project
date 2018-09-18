# api/urls.py

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = {
    url(r'^musics/create/$', views.CreateView.as_view(), name="create"),
    url(r'^musics/(?P<pk>\d+)/update/$', views.UserUpdateView.as_view(), name="music_update"),
    url(r'^musics/(?P<pk>\d+)/delete/$', views.UserDeleteView.as_view(), name="music_delete"),
    url(r'^musics/$', views.UsersListView.as_view(), name="music_list"),
}

urlpatterns = format_suffix_patterns(urlpatterns)