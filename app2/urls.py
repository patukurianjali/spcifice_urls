from app2.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('vani/',vani,name='vani'),
    path('gnani/',gnani,name='gnani'),
]