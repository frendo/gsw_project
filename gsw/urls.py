from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from .views import home, home_files, sw_js

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
     	home_files, name='home_files'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
	url(r'^accounts/', include('allauth.urls')),
	url(r'^service-worker(.*.js)$', sw_js, name='sw_js'),
]

#urlpatterns += static(settings.base.MEDIA_URL, document_root=settings.base.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    # Examples:
    # url(r'^$', 'gsw.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'', include('gsw.apps.blog.urls')),
    url(r'^$', home, name='home'),
    url(r'^blog/', include('gsw.apps.blog.urls')),
    url(r'^projects/', include('gsw.apps.projects.urls')),
    url(r'^angular/', include('gsw.apps.angular.urls')),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

