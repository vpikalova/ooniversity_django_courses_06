from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def quadratic_results(request, a, b, c):
		d = int(b) ** 2 - 4 * int(a) * int(c)
		if d < 0:
			return render(request, 'templates/results.html', {'a': a, 'b': b, 'c': c, 'd': d})
#			return HttpResponse('Квадратное уравнение a*x*x + b*x + c = 0'+ '</br>' + 
#								'<ul>' +
#								'<li> a = {}'.format(a) + '</li>' +
#								'<li> b = {}'.format(b) + '</li>' +
#								'<li> c = {}'.format(c) + '</li>' +
#								'</ul>' +
#								'Дискриминант: {}'.format(d) + '</br></br>' + 
#								'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.')
#		elif d == 0:
#			x = (-int(b)+(d)**0.5)/(2*int(a))
#			return HttpResponse('Квадратное уравнение a*x*x + b*x + c = 0'+ '</br>' + 
#								'<ul>' +
#								'<li> a = {}'.format(a) + '</li>' +
#								'<li> b = {}'.format(b) + '</li>' +
#								'<li> c = {}'.format(c) + '</li>' +
#								'</ul>' +
#								'Дискриминант: {}'.format(d) + '</br></br>' + 
#								'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {}'.format(d))
#		else:
#			x1 = (-int(b)+(d)**0.5)/(2*int(a))
#			x2 = (-int(b)-(d)**0.5)/(2*int(a))
#			return HttpResponse('Квадратное уравнение a*x*x + b*x + c = 0'+ '</br>' + 
#								'<ul>' +
#								'<li> a = {}'.format(a) + '</li>' +
#								'<li> b = {}'.format(b) + '</li>' +
#								'<li> c = {}'.format(c) + '</li>' +
#								'</ul>' +
#								'Дискриминант: {}'.format(d) + '</br></br>' + 
#								'Квадратное уравнение имеет два действительных корня x1= {}, x2= {}'.format(x1, x2))
	
