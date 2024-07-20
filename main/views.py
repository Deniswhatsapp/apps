from django.shortcuts import render
from .models import Task

# youtube.com/watch?v=6K83dgjkQNw&t=2977s lesson
# getbootstrap.com/docs/5.3/examples/ обложки
# bootstrapcdn.com/ стили


def index(request):
    tasks = Task.objects.all()
    '''
    render() этот метод указывает какой HTML шаблон нужно использовать в этой функции
    первым параметром обязательно предаем request
    вторым параметром указываем сам HTML шаблон
    ! все шаблоны дожны храниться в папке templates !
    '''
    return render(request, 'main/index.html', {'title': 'Home page'})


def about(request):
    return render(request, 'main/about.html')