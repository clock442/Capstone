from django.urls import path
from . import views

app_name = 'routeapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('gyms/', views.gyms, name='gyms'),
    path('getgyms/', views.getgyms, name='getgyms'),
]