from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import UserForm, LoginForm
import requests
from django.contrib.auth.decorators import login_required
import django.contrib.auth
from routeflash import secrets
from django.contrib.auth.models import User
from .models import Gym, Route, WallType, HoldType

def index(request):
    return render(request, 'routeapp/index.html')

def register(request):
    if request.method == 'POST':
        recaptcha_data = {
            'response': request.POST['g-recaptcha-response'],
            'secret': secrets.recaptcha_secret_key
        }
        response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=recaptcha_data)

        
        if (response.json()['success'] == False):
            message = 'failed_recaptcha'
            return render(request, 'routeapp/register.html', {'message': message})

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            message = 'user_exists'
            return render(request, 'routeapp/register.html', {'message': message})
        
        user = User.objects.create_user(username, email, password)
        django.contrib.auth.login(request, user)
        return HttpResponseRedirect(reverse('routeapp:index'))
    else:
        form = UserForm()
    return render(request, 'routeapp/register.html', {'form': form})

def login(request):
    message = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = django.contrib.auth.authenticate(request, username=username, password=password)
        if user is None:
            message = 'not_found'
        else:
            django.contrib.auth.login(request, user)
            next = request.GET.get('next', reverse('routeapp:index'))
            return HttpResponseRedirect(next)





    else:
        form = LoginForm()

    return render(request, 'routeapp/login.html', {'form': form, 'message': message})

@login_required
def logout(request):
    django.contrib.auth.logout(request)
    return HttpResponseRedirect(reverse('routeapp:login'))

def gyms(request):
    return render(request, 'routeapp/gyms.html')

def getgyms(request):
    gym_list = Gym.objects.order_by('name')
    data = []
    for gym in gym_list:
        data.append({
            'id': gym.id,
            'name': gym.name,
            'address': gym.address
        })

    return JsonResponse({'gyms': data})