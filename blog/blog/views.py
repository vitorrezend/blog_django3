from django.shortcuts import render
from website.models import Post

def hello_blog(request):
    lista = [
        'Home',
        'Podcast',
        'Personagens',
        'Cenários',
        'RPG',
    ]

    list_posts = Post.objects.all()

    data = {
        'Nome': 'Blog Django 3',
        'lista_tecnologias': lista,
        'posts': list_posts
    }

    return render(request, 'index.html', data)