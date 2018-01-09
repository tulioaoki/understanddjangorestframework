from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^$', views.home.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.api_list.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
