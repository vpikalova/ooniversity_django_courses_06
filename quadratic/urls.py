from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^results/?a=(?P<a>[0-9]+)&b=(?P<b>[0-9]+)&c=(?P<c>[0-9]+)/$', views.quadratic_results, name='quadratic_results'),
    url(r'^results/$', views.quadratic_results, name='quadratic_results'),
]