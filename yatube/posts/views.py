from django.shortcuts import render, get_object_or_404
from .models import Group, Post
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


def group_posts(request, slug):
    templates = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, templates, context)
