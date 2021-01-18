from django.shortcuts import render
from .models import *
# Create your views here.
def samples_list(request):
    samples = Sample.objects.all()
    return render(request, 'lims/index.html', context={'samples':samples})