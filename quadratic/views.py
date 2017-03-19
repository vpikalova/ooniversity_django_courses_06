#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from math import sqrt
from django.http import QueryDict


def quadratic_results(request):

    def validate(data):
        number = data
        if number == str():
            error_message = 'коэффициент не определен'
        else:
            try:
                number = int(data)
                error_message = str()
            except:
                error_message = 'коэффициент не целое число'
        return error_message, number

    arguments_from_url = request.GET
    a = arguments_from_url['a'] if arguments_from_url.__contains__('a') else str()
    b = arguments_from_url['b'] if arguments_from_url.__contains__('b') else str()
    c = arguments_from_url['c'] if arguments_from_url.__contains__('c') else str()
    error_message_a, a = validate(a)
    error_message_b, b = validate(b)
    error_message_c, c = validate(c)

    if a == 0:
        error_message_a = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
        discriminant, result = str()
    elif a == str() or b == str() or c == str():
        discriminant, result = str()
    else:
        discriminant = b * b - 4 * a * c
        if discriminant < 0:
            result = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
        elif discriminant == 0:
            x1 = -b / (2 * a)
            result = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {x1}'.format(x1=str(x1))
        elif discriminant > 0:
            x1 = (-b + sqrt(discriminant)) / (2 * a)
            x2 = (-b - sqrt(discriminant)) / (2 * a)
            result = 'Квадратное уравнение имеет два действительных корня: x1 = {x1}, x2 = {x2}'.format(x1=str(x1), x2=str(x2))

        if discriminant != str():
            discriminant = 'Дискриминант: {discriminant}'.format(discriminant=str(discriminant))

    return render(request, 'quadratic/results.html', {
        'a': a,
        'b': b,
        'c': c,
        'error_message_a': error_message_a,
        'error_message_b': error_message_b,
        'error_message_c': error_message_c,
        'discriminant': discriminant,
        'result': result
    })