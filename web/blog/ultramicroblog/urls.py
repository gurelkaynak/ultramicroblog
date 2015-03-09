from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views as ultramicroblog_views

urlpatterns = patterns('ultramicroblog.views',
    url(r'^post_list/$', ultramicroblog_views.PostList.as_view(), name="post_list"),
    url(r'^post/(?P<pk>\d+)/$', ultramicroblog_views.PostDetail.as_view(), name="post_detail"),
)

urlpatterns = format_suffix_patterns(urlpatterns)
