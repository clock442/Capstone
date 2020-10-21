from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator


def index(request):
    return HttpResponse('hello world')

