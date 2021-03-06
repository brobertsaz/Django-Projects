from django.conf.urls.defaults import *
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cms.views.home', name='home'),
    # url(r'^cms/', include('cms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',
                                              { 'document_root': '/Downloads/tinymce/jscripts/' }),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/$', 'cms.search.views.search'),
    url(r'', include('django.contrib.flatpages.urls')),
)
