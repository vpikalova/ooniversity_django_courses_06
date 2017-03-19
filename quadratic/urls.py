from django.conf.urls import include, url
from django.contrib import admin
from .views import index, contact, student_list, student_detail
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', index, name='index'),
	url(r'^contact/$', contact, name='contact'),
	url(r'^student_list/$', student_list, name='student_list'),
	url(r'^student_detail/$', student_detail, name='student_detail'),
	url(r'', include('quadratic.urls')),
	url(r'^$', views.quadratic_results, name='results')
	url(r'^quadratic/results/(?P<c>\d+)$', views.quadratic_results, name='results'), # ?a=(?P<a>\d+)&b=(?P<b>\d+)&c=
]
