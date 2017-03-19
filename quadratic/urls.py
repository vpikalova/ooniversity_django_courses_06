from django.conf.urls import include, url
from django.contrib import admin
from .views import index, contact, student_list, student_detail
from quadratic.views import quadratic_results

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', index, name='index'),
	url(r'^contact/$', contact, name='contact'),
	url(r'^student_list/$', student_list, name='student_list'),
	url(r'^student_detail/$', student_detail, name='student_detail'),
	url(r'^quadratic/results/?a=(?P<a>\w+)&b=(?P<b>\w+)&c=(?P<c>\w+)$', quadratic_results, name='results'),
]
