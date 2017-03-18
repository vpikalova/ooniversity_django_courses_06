from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse
from . import views

urlpatterns = [
    url(r'^$', views.index, name ="index"),
    url(r'index', views.index, name ="index"),
    url(r'contact', views.contact, name = "contact"),
    url(r'student_list', views.student_list, name = "student_list"),
    url(r'student_detail', views.student_detail, name = "student_detail"),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]


