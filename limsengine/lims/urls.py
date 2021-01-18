from django.urls import path
from .views import *


urlpatterns = [
    path('', samples_list, name='samples_list_url'),
]