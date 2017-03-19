from django.shortcuts import render
from math import sqrt
#from django.http import QueryDict


def quadratic_results(request):
    def try_int(data):
        my_int = None
        if data == '':
            res = 'коэффициент не определен'
        else:
            try: 
                my_int = int(data)
                res = ''           
            except: 
                res = 'коэффициент не целое число'
        return res, my_int 
        
    url_data = request.GET
    res_a, a = try_int(url_data['a'])
    res_b, b = try_int(url_data['b'])    
    res_c, c = try_int(url_data['c'])
    if a == 0:
        res_a = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
        my_discr = ''
        res_qadr = ''
    elif a == None or b == None or c == None:
        my_discr = ''
        res_qadr = ''
    else:
        my_discr = b*b - 4*a*c
        if my_discr < 0:
            res_qadr = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
        elif my_discr == 0:
            x1 = -b /(2 * a)
            res_qadr = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = ' + str(x1)
        elif my_discr > 0:
            x1 = (-b + sqrt(my_discr)) / (2 * a)
            x2 = (-b - sqrt(my_discr)) / (2 * a)
            res_qadr = 'Квадратное уравнение имеет два действительных корня: x1 = ' + str(x1) + ', x2 = '+ str(x2)

    if my_discr != '':
        my_discr = 'Дискриминант: ' + str(my_discr)

    return render(request, 'results.html', {
            'a': url_data['a'],
            'b': url_data['b'],
            'c': url_data['c'],
            'res_a': res_a,
            'res_b': res_b,
            'res_c': res_c,
            'discr': my_discr,
            'res_qadr': res_qadr
        })
