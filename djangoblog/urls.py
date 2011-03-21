from django.conf.urls.defaults import *
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	(r'^admin/', include(admin.site.urls)),

	(r'^blog/', include('djangoblog.blog.urls')),

	(r'^tags/(?P<slug>[a-zA-Z0-9_.-]+)/$', 'djangoblog.tag_views.tag_detail'),

)
