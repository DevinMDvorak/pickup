from django.conf.urls import patterns, url, include
from webapp import views

urlpatterns = patterns('',
						url(r'^$', views.index, name='index'),
						url(r'^register/$', views.register, name='register'),
						url(r'^login/$', views.user_login, name='login'),
						url(r'^logout/$', views.user_logout, name='logout'),
						url(r'^messages/', include('postman.urls', namespace='postman', app_name='postman')),
                        url(r'^newgame/$', views.creategame, name='newgame'),
						url(r'^updateprofile/$', views.updateprofile, name='update profile'),
						)