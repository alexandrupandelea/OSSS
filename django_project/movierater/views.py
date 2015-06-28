from django.shortcuts import render


def movie_list(request):
	return render(request, 'movierater/movie_list.html', {})