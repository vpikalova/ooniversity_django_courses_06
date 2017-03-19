from django.http import HttpResponse
from django.shortcuts import render
import math





def index(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def student_list(request):
    return render(request, "student_list.html")

def student_detail(request):
    return render(request, "student_detail.html")


'''def quadratic_results(request):
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    #return HttpResponse(a)'''
    
    #descr = b ** 2 -4 * a * c
    #if descr == 0:
        #x = (-b + math.sqrt(d)) / (2 * a)
    #elif descr < 0 :
        #return 'Дискриминант: -8' , 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    #else:
        #x1 = (-b + math.sqrt(d)) / (2 * a) 
        #x2 = (-b - math.sqrt(d)) / (2 * a)
        #return x1, x2""""
    
