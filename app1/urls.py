from app1.views import *

from django.urls import path

app_name='something'

urlpatterns=[
    path('virat/',virat,name='virat'),
    path('anjali/',anjali,name='anjali'),
]