from django.shortcuts import render
from .models import Movie
from .models import Rating

def movie_list(request):
	movies = Movie.objects.order_by('title')
	return render(request, 'movierater/movie_list.html', {'movies': movies})