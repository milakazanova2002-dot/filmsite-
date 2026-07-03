from django.http import Http404, HttpResponse
from django.shortcuts import render


FILMS = {
    1: 'Крёстный отец',
    2: 'Список Шиндлера',
    3: 'Побег из Шоушенка',
}


def index(request):
    return HttpResponse('Добро пожаловать на сайт фильмов!')


def about(request):
    return HttpResponse('Сайт-каталог фильмов. Здесь собраны лучшие фильмы всех времён.')


def film_list(request):
    genre = request.GET.get('genre', '')      # ?genre=drama
    year = request.GET.get('year', '')        # ?year=2020
    
    response_text = f'Жанр: {genre}, год: {year}' if genre or year else 'Все фильмы'
    return HttpResponse(response_text)


def film_detail(request, film_id):
    if film_id not in FILMS:
        raise Http404(f'Фильм с id={film_id} не найден')
    
    return HttpResponse(f'Фильм: {FILMS[film_id]}')


def films_by_year(request, year, page):
    return HttpResponse(f'Фильмы {year} года, страница {page}')


def director_detail(request, director_id):
    return HttpResponse(f'Страница режиссёра с id={director_id}')


# ошибки
def page_not_found(request, exception):
    return HttpResponse('Страница не найдена. Вернитесь на главную.', status=404)


def server_error(request):
    return HttpResponse('Произошла ошибка сервера. Мы уже работаем над этим.', status=500)

