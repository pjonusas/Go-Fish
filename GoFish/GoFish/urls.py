from django.conf.urls import patterns, include, url
from django.contrib import admin
from game import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^lobby$', views.lobby, name='lobby'),
    url(r'^ready$', views.ready, name='ready'),
    url(r'^ready2$', views.ready2, name='ready2'),
    url(r'^create_post/$', views.create_post, name='create_post'),
    url(r'^lobby/(?P<game_id>[0-9]+)/$', views.lobby, name='lobby'),
    url(r'^game$', views.game, name='game'),
    url(r'^game/(?P<game_id>[0-9]+)/$', views.game, name='game'),
)
