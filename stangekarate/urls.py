from django.conf.urls.defaults import *
from django.contrib import admin
from cms.sitemaps import CMSSitemap
from cmsplugin_blog.sitemaps import BlogSitemap


admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^test_project/', include('test_project.foo.urls')),

    url(r'^getAllSponsors/$', 'stangekarate.sponsorApp.views.getAllSponsors'),
    url(r'^getSponsor/$', 'stangekarate.sponsorApp.views.getSponsor'),
    ('^admin/', include(admin.site.urls)),
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {
        'sitemaps': {
            'cmspages': CMSSitemap,
            'blogentries': BlogSitemap
        }
    }),
    url(r'^', include('cms.urls')),
)
