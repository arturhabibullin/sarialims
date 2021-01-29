from django.urls import path
from .views import *


urlpatterns = [
    path('', samples_list, name='samples_list_url'),
    path('sample/<int:pk>/', sample_detail, name='sample_detail_url'),
    path('categorys/', categorys_list, name='categorys_list_url'),
    path('category/<int:pk>/', category_detail, name='category_detail_url'),
]