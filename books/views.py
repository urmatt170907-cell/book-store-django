from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def home_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello World')
    
def books_detail_view(request):
    if request.method == 'GET':
        context = {
            'title': 'Белый Клык',
            'name': 'Джек Лондон',
            'time': datetime.now(),
            'capabilities': [
                'Часть первая: Дикая глушь',
                'Часть вторая: Рожденный в логово',
                'Часть третья: Бог Дикарей',
                'Часть четвертая: Ненавистный хозяин',
                'Часть пятая: Ручной волк'
            ]
        }
        return render(request, 'books_detail.html', context)
