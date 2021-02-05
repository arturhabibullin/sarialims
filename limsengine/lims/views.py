from django.shortcuts import render
from .models import *
# Create your views here.
def samples_list(request):
    samples = Sample.objects.all().order_by('-date_production')
    return render(request, 'lims/index.html', context={'samples': samples})

def sample_detail(request, pk):
    sample = Sample.objects.get(pk=pk)
    return render(request, 'lims/sample_detail.html', context={'sample': sample})

def categorys_list(request):
    categorys = Category.objects.all()
    return render(request, 'lims/categorys_list.html', context={'categorys': categorys})    

def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    return render(request,'lims/category_detail.html', context={'category': category})