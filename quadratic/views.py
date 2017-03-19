import math

from django.shortcuts import render

MSG_NOT_DEFINED = 'коэффициент не определен'
MSG_NOT_INT = 'коэффициент не целое число'
MSG_A_IS_ZERO = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'


def quadratic_results(request):
    vars = {
        'a': request.GET.get('a', ''),
        'b': request.GET.get('b', ''),
        'c': request.GET.get('c', '')
    }
    errors = False
    for key in vars.keys():
        if vars[key] != "":
            try:
                vars[key] = int(vars[key])
                print(vars[key])
                if key == 'a' and vars[key] == 0:
                    vars[key] = str(vars[key]) + "<br /><i>%s</i>" % MSG_A_IS_ZERO
                    errors = True
            except ValueError:
                vars[key] = vars[key] + "<br /><i>%s</i>" % MSG_NOT_INT
                errors = True
        else:
            vars[key] = vars[key] + "<br /><i>%s</i>" % MSG_NOT_DEFINED
            errors = True
    if not errors:
        a = vars['a']
        b = vars['b']
        c = vars['c']
        message = str()
        d = b ** 2 - 4 * a * c
        vars['d'] = d
        if d >= 0:
            x1 = (-b + math.sqrt(d)) / 2 * a
            x2 = (-b - math.sqrt(d)) / 2 * a
            message = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: " \
                      "x1 = x2 = %s" % x1 if d == 0 else \
                      "Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s" % (x1, x2)
        else:
            message = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
        vars['message'] = message
    return render(request, 'results.html', vars)
