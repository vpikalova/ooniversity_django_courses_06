from django.conf.urls import url

from . import views

#app_name = 'quadratic'
urlpatterns = [
    url(r'^result/$', views.quadratic_results, name='results'),
]