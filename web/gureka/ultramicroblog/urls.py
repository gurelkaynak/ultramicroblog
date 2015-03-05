from django.conf.urls import patterns, url

urlpatterns = patterns('ultramicroblog.views',
    url(r'^$',
        'list_view',
        name="blog_index"),
    url(r'^posts/(?P<post_id>\d+)/$',
        'detail_view',
        name="blog_detail"),
)
