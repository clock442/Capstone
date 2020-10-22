from django.urls import path
from . import views

app_name = 'routeflash'

urlpatterns = [
    path('', views.index, name='index'),
]