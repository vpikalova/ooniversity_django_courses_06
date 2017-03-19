#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import render_to_response


def quadratic_results(request):
	values = {
		'a': request.GET.get('a'),
		'b': request.GET.get('b'),
		'c': request.GET.get('c')}

	response = {}

	for key in values.keys():
		if len(values[key]) == 0:
			response[key] = 'коэффициент не определен'
		else:
			try:
				response[key] = int(values[key])
			except ValueError:
				response[key] = 'коэффициент не целое число'

	if values['a'] == '0':
		response['a'] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
	try:
		a, b, c = int(response['a']), int(response['b']), int(response['c'])

		discriminant = b ** 2 - 4 * a * c
		print(discriminant)
		if discriminant < 0:
			message = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
		elif discriminant == 0:
			message = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный \
															корень: x1 = x2 = {0}'.format(-b/2*a)
		else:
			x1 = (-b + discriminant**0.5 / 2 * a)
			x2 = (-b - discriminant**0.5 / 2 * a)
			message = 'Квадратное уравнение имеет два действительных \
					   корня: x1 = {0}, x2 = {0}'.format(x1, x2)
	except ValueError:

		return render(request, 'results.html', {
				      'a': values['a'], 'b': values['b'], 'c': values['c'], 
				      'info_a': response['a'], 'info_b': response['b'], 'info_c': response['c']})


	return render(request, 'results.html', {
				      'a': values['a'], 'b': values['b'], 'c': values['c'], 
				      'info_a': '', 'info_b': '', 'info_c': '', 'discriminant': discriminant,
				      'message': message})


		


