from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^all/$', 'article.views.articles'),
    url(r'^get/(?P<article_id>\d+)/$', 'article.views.article'),
    url(r'^commands/$', 'article.views.commands'),
    url(r'^last/$', 'article.views.last_entry'),
    url(r'^last_id/$', 'article.views.last_entry_id'),
	

    url(r'^file_upload/$', 'article.views.file_upload'),
    url(r'^all_files/$', 'article.views.files'),
    url(r'^get_file/(?P<article_id>\d+)/$', 'article.views.file_'),
	
	url(r'^get_tram_file/$', 'article.views.tram_file'),
	url(r'^tram_file_upload/$', 'article.views.tram_file_upload'),
	
    #url(r'^download/$', 'article.views.file_'),
)

urlpatterns += staticfiles_urlpatterns()