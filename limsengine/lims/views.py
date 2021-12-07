from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import get_object_or_404
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required



@login_required(login_url='login_url')
def company_detail(request, slug):
    company = Company.objects.get(slug=slug)
    samples = company.sample_set.all()
    paginator = Paginator(samples, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    is_paginated = page_obj.has_other_pages()
    if page_obj.has_previous():
        prev_url = '?page={}'.format(page_obj.previous_page_number())
    else:
        prev_url = ''
    if page_obj.has_next():
        next_url = '?page={}'.format(page_obj.next_page_number())
    else:
        next_url = ''
    products = Product.objects.filter(sample__company__slug=slug).distinct()
    context = {
        'company':company,
        'page_obj':page_obj,
        'is_paginated':is_paginated,
        'next_url':next_url,
        'prev_url': prev_url,
        'products':products
       
    }
    return render(request, 'lims/company_detail.html', context)


@login_required(login_url='login_url')
def tags_list(request):
    tags = Tag.objects.all()
    context = {
        'tags':tags,
    }
    return render(request, 'lims/tags_list.html', context)

@login_required(login_url='login_url')
def tag_detail(request, slug):
    tag = Tag.objects.get(slug=slug)
    samples = tag.samples.all()
    paginator = Paginator(samples, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    is_paginated = page_obj.has_other_pages()
    if page_obj.has_previous():
        prev_url = '?page={}'.format(page_obj.previous_page_number())
    else:
        prev_url = ''
    if page_obj.has_next():
        next_url = '?page={}'.format(page_obj.next_page_number())
    else:
        next_url = ''
    context = {
        'page_obj':page_obj,
        'is_paginated':is_paginated,
        'next_url':next_url,
        'prev_url': prev_url,
    }
    return render(request, 'lims/tag_detail.html', context)



# def product_detail(request, slug):
#     product = Product.objects.get(slug=slug)
#     sample=product.sample_set.all()
#     context = {
#         'product':product,
#         'sample':sample
#     }
#     return render(request, 'lims/product_detail.html', context)
@login_required(login_url='login_url')
def samples_list(request):
    samples = Sample.objects.all()
    paginator = Paginator(samples, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    is_paginated = page_obj.has_other_pages()
    if page_obj.has_previous():
        prev_url = '?page={}'.format(page_obj.previous_page_number())
    else:
        prev_url = ''
    if page_obj.has_next():
        next_url = '?page={}'.format(page_obj.next_page_number())
    else:
        next_url = ''
    companys = Company.objects.all()
    context = {
        'page_obj':page_obj,
        'is_paginated':is_paginated,
        'next_url':next_url,
        'prev_url': prev_url,
        'companys':companys,
    }
    return render(request, 'lims/samples_list.html', context)


@login_required(login_url='login_url')
def sample_detail(request, sample):
    sample = Sample.objects.get(sample=sample)
    company = sample.company
    product = sample.product
  
    context = {
        'sample':sample,
        'company':company,
        'product':product,
        
    }
    return render(request, 'lims/sample_detail.html', context)

@login_required(login_url='login_url')
def company_product(request,company, product):
    company = Company.objects.get(slug=company)
    product = Product.objects.get(slug=product)
    samples = Sample.objects.filter(company=company,product=product)
    paginator = Paginator(samples, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    is_paginated = page_obj.has_other_pages()
    if page_obj.has_previous():
        prev_url = '?page={}'.format(page_obj.previous_page_number())
    else:
        prev_url = ''
    if page_obj.has_next():
        next_url = '?page={}'.format(page_obj.next_page_number())
    else:
        next_url = ''
    tags = Tag.objects.filter(samples__company__slug=company.slug, samples__product__slug=product.slug).distinct()
    materials = Material.objects.filter(sample__company__slug=company.slug, sample__product__slug=product.slug).distinct()
    context = {
        'page_obj':page_obj,
        'is_paginated':is_paginated,
        'next_url':next_url,
        'prev_url': prev_url,
        'tags':tags,
        'company':company,
        'materials':materials,
        'product':product,
    }
    return render(request, 'lims/company_product.html', context)

# def company_tag(request, company, tag):
#     company = Company.objects.get(slug=company)
#     tag = Tag.objects.get(slug=tag)
#     samples = Sample.objects.filter(company=company, tag=tag)
#     paginator = Paginator(samples, 1)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     is_paginated = page_obj.has_other_pages()
#     if page_obj.has_previous():
#         prev_url = '?page={}'.format(page_obj.previous_page_number())
#     else:
#         prev_url = ''
#     if page_obj.has_next():
#         next_url = '?page={}'.format(page_obj.next_page_number())
#     else:
#         next_url = ''
#     context = {
#         'page_obj':page_obj,
#         'is_paginated':is_paginated,
#         'next_url':next_url,
#         'prev_url': prev_url,
#         'company':company,
#     }
#     return render(request, 'lims/company_tag.html', context)
@login_required(login_url='login_url')
def company_product_material(request, company, product, material):
    company = Company.objects.get(slug=company)
    product = Product.objects.get(slug=product)
    material = Material.objects.get(slug=material)
    samples = Sample.objects.filter(company=company, product=product, material=material)
    paginator = Paginator(samples, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    is_paginated = page_obj.has_other_pages()
    if page_obj.has_previous():
        prev_url = '?page={}'.format(page_obj.previous_page_number())
    else:
        prev_url = ''
    if page_obj.has_next():
        next_url = '?page={}'.format(page_obj.next_page_number())
    else:
        next_url = ''
    tags = Tag.objects.filter(samples__company__slug=company.slug, samples__product__slug=product.slug, samples__material__slug=material.slug).distinct()
    context = {
        'company':company,
        'product':product,
        'material':material,
        'page_obj':page_obj,
        'is_paginated':is_paginated,
        'next_url':next_url,
        'prev_url': prev_url,
        'tags':tags,
    }
    return render(request, 'lims/company_product_material.html', context)
    
@login_required(login_url='login_url')
def company_product_material_tag(request, company, product, material, tag):
    company = Company.objects.get(slug=company)
    product = Product.objects.get(slug=product)
    material = Material.objects.get(slug=material)
    tag = Tag.objects.get(slug=tag)
    samples = Sample.objects.filter(company=company, product=product, material=material, tags=tag)
    paginator = Paginator(samples, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    is_paginated = page_obj.has_other_pages()
    if page_obj.has_previous():
        prev_url = '?page={}'.format(page_obj.previous_page_number())
    else:
        prev_url = ''
    if page_obj.has_next():
        next_url = '?page={}'.format(page_obj.next_page_number())
    else:
        next_url = ''
    context = {
        'page_obj':page_obj,
        'is_paginated':is_paginated,
        'next_url':next_url,
        'prev_url': prev_url,
    }
    return render(request, 'lims/company_product_material_tag.html', context)



