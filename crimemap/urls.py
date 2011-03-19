from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^crime/([A-Za-z]+)', 'crimemap.mapper.views.crime_by_type'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
)
