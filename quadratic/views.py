from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def quadratic_results(request, a, b, c):
#	if 
#		return HttpResponseNotFound('<h1>Error<h1>')
#	if int(a) and int(b) and int(c):
		d = int(b) ** 2 - 4 * int(a) * int(c)
		if d < 0:
			return HttpResponse('Квадратное уравнение a*x*x + b*x + c = 0'+ '</br>' + 
								'<ul>' +
								'<li> a = ' + str(a) + '</li>' +
								'<li> b = ' + str(b) + '</li>' +
								'<li> c = ' + str(c) + '</li>' +
								'</ul>' +
								'Дискриминант: ' + str(d) + '</br></br>' + 
								'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.')
		elif d == 0:
			x = (-int(b)+(d)**0.5)/(2*int(a))
			return HttpResponse('Квадратное уравнение a*x*x + b*x + c = 0'+ '</br>' + 
								'<ul>' +
								'<li> a = ' + str(a) + '</li>' +
								'<li> b = ' + str(b) + '</li>' +
								'<li> c = ' + str(c) + '</li>' +
								'</ul>' +
								'Дискриминант: ' + str(d) + '</br></br>' + 
								'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = ' + str(x))
		else:
			x1 = (-int(b)+(d)**0.5)/(2*int(a))
			x2 = (-int(b)-(d)**0.5)/(2*int(a))
			return HttpResponse('Квадратное уравнение a*x*x + b*x + c = 0'+ '</br>' + 
								'<ul>' +
								'<li> a = ' + str(a) + '</li>' +
								'<li> b = ' + str(b) + '</li>' +
								'<li> c = ' + str(c) + '</li>' +
								'</ul>' +
								'Дискриминант: ' + str(d) + '</br></br>' + 
								'Квадратное уравнение имеет два действительных корня x1=' + str(x1) + ', x2=' + str(x2))
#	else:
#		return HttpResponseNotFound('<h1>Error<h1>')
	
