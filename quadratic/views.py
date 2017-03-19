from django.shortcuts import render
from django.http import QueryDict
from math import sqrt

def ItIsInt(**kwargs) -> dict:
    '''return 2 dict
       first - error_list
       second - given argumets if they named as "a","b" or "c" '''
    
    errors={} # dict of error strings
    args={} # int argument or raw data if not integer value given
    for key in 'abc':
        if not kwargs.get(key):
            errors[key] = "коэффициент не определен"
            args[key]='' # no data - empty arg value (prevent None)
        else:
            try:
                print(key," : ",kwargs.get(key))
                args[key] = int(kwargs[key])
                errors[key] = "" # no error - empty string value
            except ValueError:
                errors[key] = "коэффициент не целое число"
                args[key]=kwargs.get(key) # wrong data to show
    if kwargs.get('a') == '0':
        errors[key] = "коэффициент при первом слагаемом уравнения не может быть равным нулю"
    return errors, args         


def discriminant(a,b,c):
    return b*b-(4*a*c)
      
# Create your views here.
def quadratic_results(request):
    print(request.GET.dict())
    error_list,value_list=(ItIsInt(**request.GET.dict()))
    print("err-lst=",error_list,'\narg-lst=',value_list)
    D=discriminant(*value_list.values())
    print("deskr=",D)
    #if a
    #context = {'first': a, 'second': b, 'free_set': c}
    return render(request, 'quadratic/results.html',request.GET.dict())#, context)