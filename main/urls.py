from django.conf.urls.defaults import *

urlpatterns = patterns('django_app.main.views',
    url(r'^$','index',name='index')
)
