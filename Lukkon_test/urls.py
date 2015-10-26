from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('photo.urls')),
    url(r'login/$', 'django.contrib.auth.views.login', name='login_url'),
    url(r'logout/$', 'django.contrib.auth.views.logout', {
        'next_page': '/login/',
    }, name='logout_url'),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
)
# Test comment
# change
