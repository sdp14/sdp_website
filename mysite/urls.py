from django.conf.urls import patterns, include, url
from mysite.views import hello, post_logout
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', hello),
	url(r'^post_logout/$', post_logout),
    (r'^articles/', include('article.urls')),
	(r'^data/', include('data.urls')),
	(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
	(r'^accounts/logout/$', 'django.contrib.auth.views.logout',{'next_page': '/post_logout/'}),
)

