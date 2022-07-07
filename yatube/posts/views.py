from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    templates = 'posts/index.html'
    return render(request, templates)

def group(request):
    return HttpResponse('Список групп')

def group_posts(requst, slug):
    return HttpResponse(f'Группа: {slug}')


