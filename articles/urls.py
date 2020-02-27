from django.conf.urls import url
from .import views


app_name = "blog"

urlpatterns = [
    url(r'^$', views.article_list, name="list"), 
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="post"),
]
