from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import math
# Create your views here.

 

def quadratic_results(request):
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    error = ''
    error_a = ''
    error_b = ''
    error_c = ''
    x = 0
    x1 = 0
    x2 = 0
    descr = None
    out_string = ''
    if not a:
        error_a = 'коэффициент не определен'
    
    else:

        try:
            a = int(a)
        
        except ValueError:
            error_a = 'коэффициент не целое число'
        else:
            a = int(a)
    print(error)

    if not b:
        error_b = 'коэффициент не определен'
    
    else:

        try:
            b = int(b)
        
        except ValueError:
            error_b = 'коэффициент не целое число'
        else:
            b = int(b)
    print(error)
    
    if not c:
        error_c = 'коэффициент не определен'
    
    else:

        try:
            c = int(c)
        
        except ValueError:
            error_c = 'коэффициент не целое число'
        else:
            c = int(c)
    print(error)
    if a == 0:
        error_a = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'    
        
    if type(a) ==int  and type(b)==int and type(c) == int and a!=0:

        descr = b ** 2 - 4 * a * c
    
        if descr == 0:
            x = (-int(b) + math.sqrt(descr)) / (2 * int(a))
            out_string =  'Дискриминант: 0'
        elif descr < 0 :
            out_string =  'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
        else:
            x1 = (-b + math.sqrt(descr)) / (2 * a) 
            x2 = (-b - math.sqrt(descr)) / (2 * a)
        
    return render(request, "results.html", {"input_a" :a, "input_b":b, "input_c":c, 'x1':x1, 'x2':x2, 'error':error, 'out_string':out_string, 'descr':descr, 'error_a':error_a, 'error_b':error_b, 'error_c':error_c })


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
    
