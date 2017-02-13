from django.conf.urls import url

from . import views

app_name = 'member_resources'

urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    # ex: /songs/5/
    url(r'^songs/$', views.SongListView.as_view(), name='song_list'),
    # ex: /songs/5/
    url(r'^songs/(?P<pk>[0-9]+)/$', views.SongView.as_view(), name='song'),
    # ex: /choir_members/
    url(r'^choir_members/$', views.choir_member_list_view, name='choir_member_list'),
    # ex: /choir_members/5/
    url(r'^choir_members/(?P<choir_member_id>[0-9]+)/$', views.choir_member_view, name='choir_member'),
    # # ex: /choir_members/5/song/2
    # url(r'^(?P<choir_member_id>[0-9]+)/song/$', views.song_parts, name='song'),
]
