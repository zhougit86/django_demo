from django.conf.urls import url
from django.views.generic import TemplateView as template

from . import views


urlpatterns = [
    url(r'^$',
        template.as_view(template_name='guys/guys.html'),
        name='index'),
    # url(r'^(?P<pk>\d+)/$', views.guy_detail.as_view(), name='view_guy'),
]