from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    templates = 'posts/index.html'
    title = 'Главная страница'
    text = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, templates, context)

def group_list(request):
    templates = 'posts/group_list.html'
    title = 'Группы'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, templates, context)

def group(requst, slug):
    return HttpResponse(f'Группа: {slug}')


