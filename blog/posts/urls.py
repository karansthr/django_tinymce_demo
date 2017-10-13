
from django.conf.urls import url
from .views import post_create,post_edit,post_list,post_detail

urlpatterns = [
        url(r'^posts/(?P<id>\d+)$',post_detail,name="detail"),
        url(r'^posts/(?P<id>\d+)/edit/$',post_edit),
        url(r'^create/$', post_create),
        url(r'^$',post_list),
]
