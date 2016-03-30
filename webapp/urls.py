from django.conf.urls import patterns, url, include
from webapp import views
from pickup import settings

urlpatterns = patterns('',
						url(r'^$', views.index, name='index'),
						url(r'^register/$', views.register, name='register'),
						url(r'^login/$', views.user_login, name='login'),
						url(r'^logout/$', views.user_logout, name='logout'),
						url(r'^messages/', include('postman.urls', namespace='postman', app_name='postman')),
                        url(r'^newgame/$', views.creategame, name='newgame'),
                        url(r'^groups/$', views.groups, name='groups'), # Create groups
						url(r'^groupslist/$', views.groups_list, name='groupslist'), # View list of groups
						url(r'^(?P<group_id>[0-9]+)/group/$', views.group, name='group'), # View individual groups
                       url(r'^account/(?P<username>\w+)/$', views.profile_view, name='profile_view'),
						)
