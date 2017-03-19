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
            errors['err_'+key] = "коэффициент не определен"
            args['arg_'+key]='' # no data - empty arg value (prevent None)
        else:
            try:
                #print("!!!we in tray!!! ",key," : ",kwargs.get(key))
                args['arg_'+key] = int(kwargs[key])
                errors['err_'+key] = "" # no error - empty string value
            except ValueError:
                errors['err_'+key] = "коэффициент не целое число"
                args['arg_'+key]=kwargs.get(key) # wrong data to show
    if kwargs.get('a') == '0':
        errors[key] = "коэффициент при первом слагаемом уравнения не может быть равным нулю"
    return errors, args         


def discriminant(a,b,c):
    return b*b-(4*a*c)

def roots(discriminant,a,b) -> list:
    '''Return root(s) of quadratic equation if discriminant>=0'''
    rootlist=[]
    if discriminant > 0:
        rootlist.append((-b+sqrt(discriminant))/(2*a))
        rootlist.append((-b-sqrt(discriminant))/(2*a))
    elif discriminant == 0:
        rootlist.append(-b/(2*a))
    return rootlist
      
    
      
# Create your views here.
def quadratic_results(request):
    D=x1=x2=''
#    print(request.GET.dict())
    web_params=request.GET.dict()
    errors_dict,values_dict=(ItIsInt(**web_params))
    print("err-lst=",errors_dict,'\narg-lst=',values_dict)
    if not any(errors_dict.values()): # if no errors - calculate discriminant
        D=discriminant(*values_dict.values())
        if D >= 0: # calc roots
            try:
                x1,x2=roots(D,values_dict['arg_a'],values_dict['arg_b']) # > 0
            except ValueError:
                x1=roots(D,values_dict['arg_a'],values_dict['arg_b'])[0] # = 0
        
    #print("deskr=",D,'x1,x2=',x1,x2)
    #if a
    #context = {'first': a, 'second': b, 'free_set': c}
    # context=request.GET.dict())
    context = {**errors_dict, **values_dict,'discriminant': D,'root1': x1,'root2': x2}
    print(context)
    return render(request, 'quadratic/results.html', context)