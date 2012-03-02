from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('main.views',
    url(r'^$', 'home', name='home'),
    url(r'^zombie/(?P<pk>\d+)$', 'show_twits', name='show_twits'),
    url(r'zombie/(?P<pk>\d+)/edit$', 'edit_zombie', name='edit_zombie'),
    url(r'^zombie/add/$', 'add_zombie', name='add_zombie'),
    url(r'^zombie/(?P<pk>\d+)/delete$', 'delete_zombie', name='delete_zombie'),
    url(r'twit/(?P<pk>\d+)/edit$', 'edit_twit', name='edit_twit'),
    url(r'^twit/(?P<pk>\d+)/delete$', 'delete_twit', name='delete_twit'),
    url(r'^twit/add/$', 'add_twit', name='add_twit'),
    )
