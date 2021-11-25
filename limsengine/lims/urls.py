from django.urls import path
from .views import *


urlpatterns = [
    path('', samples_list, name='samples_list_url'),
    path('sample/<str:sample>/', sample_detail, name='sample_detail_url'),
    path('company/<str:slug>/', company_detail, name='company_detail_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/<str:slug>/', tag_detail, name='tag_detail_url'),
    # path('product/<str:slug>/', product_detail, name='product_detail_url'),
    path('company-product/<str:company>/<str:product>/', company_product, name='company_product_url'),
    # path('company-tag/<str:company>/<str:tag>/', company_tag, name='company_tag_url'),
    path('company-product-material/<str:company>/<str:product>/<str:material>/', company_product_material, name='company_product_material_url'),
    path('company-product-material-tag/<str:company>/<str:product>/<str:material>/<str:tag>/', company_product_material_tag, name='company_product_material_tag_url'),
]