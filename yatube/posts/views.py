from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def index(request):
    templates = 'posts/index.html'
    title = 'Главная страница'
    text = 'Это главная страница проекта Yatube'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title': title,
        'text': text,
        'posts': posts,
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


