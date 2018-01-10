from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^$', views.SubsList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.SubsDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
