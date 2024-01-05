from django.shortcuts import render

def index(request):
    return render(
        request,
        'mainpage/spisok_del.html'
    )

import todo  # Это название вашего проекта

def get_menu(active):
    result = []
    for elem in swx.urls.navset:
        if elem['url'] == active:
            elem['active'] = True
        result.append(elem)
    return result

def index(request):
    context = {
         'navset': get_menu('/'),
    }
    return render(
        request,
        'mainpage/index.html',
        context)

