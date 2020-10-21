from django.urls import path
from . import views

app_name = 'rockapp'

url_patterns = [
    path('', views.index, name='index'),
]