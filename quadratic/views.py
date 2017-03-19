from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import math
# Create your views here.

 

def quadratic_results(request):
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    error = ''
    x = 0
    x1 = 0
    x2 = 0
    descr = 0
    out_string = ''
    if a is None or b is None or c is None :
        error = 'коэффициент не определен'
    '''elif type(a) != int or  type(b) != int or  type(c) != int:'''
    try:
        a = int(a)
    except TypeError:
        error = 'коэффициент не целое число'
    except ValueError:
        error = 'коэффициент не определен'
    try:
        b = int(b)
    except TypeError:
        error = 'коэффициент не целое число'
    try:
        c = int(c)
    except TypeError:
        error = 'коэффициент не целое число'
        
    if a == 0:
        error = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'    
    try:   
        descr = b ** 2 - 4 * a * c
    except ValueError:
        error = 'коэффициент не определен'
    if descr == 0:
        x = (-int(b) + math.sqrt(descr)) / (2 * int(a))
        out_string =  'Дискриминант: 0'
    elif descr < 0 :
        out_string =  'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    else:
        x1 = (-b + math.sqrt(descr)) / (2 * a) 
        x2 = (-b - math.sqrt(descr)) / (2 * a)
        
    return render(request, "results.html", {"input_a" :a, "input_b":b, "input_c":c, 'x1':x1, 'x2':x2, 'error':error, 'out_string':out_string, 'descr':descr })

'''def quadratic_results(request):
    a = int(request.GET['a'])
    b = int(request.GET['b'])
    c = request.GET['c']
    return render(request, "results.html")'''


def index(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def student_list(request):
    return render(request, "student_list.html")

def student_detail(request):
    return render(request, "student_detail.html")
    
