from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$',views.guys,name='guys'),
    url(r'^(?P<guy_id>\d+)/$', views.view_guy, name='view_guy'),
]