from django.shortcuts import render


def hello_blog(request):
    lista = [
    'Home', 'Podcast', 'Personagens', 'Cenários', 'RPG',
    ]
    data = {'Nome': 'Blog Django 3', 'lista_tecnologias': lista}

    return render(request, 'index.html', data)