from django.shortcuts import render
from django.http import HttpResponse

def quadratic_results(request, a, b, c):
	d = int(b) ** 2 - 4 * int(a) * int(c)
	if d < 0:
		print(d)
		return HttpResponse('Дискриминант: ' + str(d) + '\n' + 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.')
	elif d == 0:
		print(d)
		x = (-b+(d)**0.5)/(2*a)
		#return HttpResponse('Дискриминант: ', d, '\nДискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1=x2=', x)
	else:
		print(d)
		x1 = (-b+(d)**0.5)/(2*a)
		x2 = (-b-(d)**0.5)/(2*a)
		#return HttpResponse('Дискриминант: ', d, '\nКвадратное уравнение имеет два действительных корня: x1=', x1, 'x2=', x2)
	return HttpResponse(d)
