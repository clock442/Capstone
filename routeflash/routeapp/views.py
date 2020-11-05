from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import UserForm, LoginForm
import requests
from django.contrib.auth.decorators import login_required
import django.contrib.auth
from routeflash import secrets
from django.contrib.auth.models import User
from .models import Gym, Route, WallType, HoldType
from datetime import datetime

def index(request):
    return render(request, 'routeapp/index.html')

def about(request):
    return render(request, 'routeapp/about.html')

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

def routes(request, gym_id):
    gym = Gym.objects.get(id=int(gym_id))

    context = {
        'gym': gym,
    }
    return render(request, 'routeapp/routes.html', context)

def getroutes(request, gym_id):

    route_color_dict = {
        '1': '#388e3c',
        '2': '#4caf50',
        '3': '#c6ff00',
        '4': '#ffeb3b',
        '5': '#ffb74d',
        '6': '#f57c00',
        '7': '#d32f2f',
        '8': '#ef5350',
        '9': '#f06292',
        '10': '#ab47bc',
        '11': '#64b5f6'
    }


    gym = Gym.objects.get(id=gym_id)
    route_list = gym.routes.all()
    data = []
    for route in route_list:
        data.append({
            'id': route.id,
            'name': route.name,
            'wall_type': route.wall_type.name,
            'hold_types': [hold_type.name for hold_type in route.hold_types.all()],
            'rating': route.rating,
            'height': route.height,
            'description': route.description,
            'date_created': route.date_created.strftime("%m/%d/%Y"),
            'x_position': route.x_position,
            'y_position': route.y_position,
            'rating_color': route_color_dict[str(route.rating)]
        })

    return JsonResponse({'routes': data})

