from django.conf.urls import url

from . import views


urlpatterns = [
    # url(r'^$',views.guys,name='guys'),
    # url(r'^(?P<guy_id>\d+)/$', views.view_guy, name='view_guy'),
    url(r'^$',views.guys_view.as_view(),name='guys'),
    url(r'^(?P<pk>\d+)/$', views.guy_detail.as_view(), name='view_guy'),
    # url(r'^json/$',views.guys_json),
]