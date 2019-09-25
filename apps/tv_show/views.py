import json, requests
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages
from . import models as m

API_URL = 'http://api.tvmaze.com/search/shows?q={}'

def get_request(request, url):
    response = requests.get(url)
    return json.loads(response.text)

def index(request):

    movies = []
    
    if 'user_id' in request.session:
        
        movies = m.Like.objects.filter(user_id=request.session['user_id']).order_by('-created_at')
        
        context = {
            'count' : len(movies),
            'movies' : movies
        }

    else:

        context = {
            'count' : 0,
            'movies' : movies
        }

    return render(request, 'tv_show/index.html', context)

def search(request):
    
    query = request.POST['query']

    return redirect('tv_show:results', query=query)

def results(request, query):

    url = API_URL.format(query)
    data = get_request(request, url)
    movies = []

    for obj in data:
        movie = m.Movie()
        movie.parse_json(obj)
        try:
            movie = m.Movie.objects.get(url=movie.url)
        except:

            movie.save()
        
        movies.append(movie)
    
    likes = []

    if 'user_id' in request.session:
        for like in m.Like.objects.filter(user_id=request.session['user_id']):
            likes.append(like.movie_id)

    context = {
        'liked' : likes,
        'query' : query,
        'count' : len(data),
        'movies' : movies
    }

    return render(request, 'tv_show/search.html', context)

def create_like(request, movie_id):

    url = request.META.get('HTTP_REFERER')

    try:
        like = m.Like.objects.get(movie_id=movie_id)
    except:

        like = m.Like()
        like.user_id = request.session['user_id']
        like.movie_id = movie_id
        like.save()
    
    return redirect(url)
        
def delete_like(request, movie_id):

    url = request.META.get('HTTP_REFERER')

    try:
        like = m.Like.objects.get(movie_id=movie_id)
        like.delete()
    except:
        messages.error(request, 'Unlike Movie ID {} error'.format(movie_id))

    return redirect(url)