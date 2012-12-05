from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^accounts/',include('django.contrib.auth.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'', include('django_app.main.urls')),
)

urlpatterns += staticfiles_urlpatterns()
