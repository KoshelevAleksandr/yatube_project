from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Главная страница')

def group(request):
    return HttpResponse('Список групп')

def group_posts(requst, slug):
    return HttpResponse(f'Группа: {slug}')


