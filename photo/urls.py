from django.conf.urls import url, patterns
from . import views
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', views.photo_list, name='photo_list'),
    url(r'^photo/(?P<photo_id>\d+)$', 'photo.views.single_photo', name='view_single_photo'),
    url(r'^signup/$', 'photo.views.signup', name='signup'),
    url(r'^signup_ok/$', TemplateView.as_view(
        template_name='registration/signup_ok.html'
    ), name='signup_ok'),
)