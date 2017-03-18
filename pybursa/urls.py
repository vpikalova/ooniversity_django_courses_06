from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse

def indexpage(request):
    return render(request, "index.html")

def contactpage(request):
    return render(request, "contact.html")

def student_list(request):
    return render(request, "student_list.html")

def student_detail(request):
    return render(request, "student_detail.html")


urlpatterns = [
    url(r'^$', indexpage),
    url(r'index', indexpage),
    url(r'contact', contactpage),
    url(r'student_list', student_list),
    url(r'student_detail', student_detail),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]


