from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

# from .models import Choice, Question


def index(request):
    return render(request, 'pybursa/index.html')

def contact(request):
    return render(request, 'pybursa/contact.html')

def student_list(request):
    return render(request, 'pybursa/student_list.html')

def student_detail(request):
    return render(request, 'pybursa/student_detail.html')


  #  def get_queryset(self):
    #    """Return the last five published questions."""
    #    return Question.objects.order_by('-pub_date')[:5]
