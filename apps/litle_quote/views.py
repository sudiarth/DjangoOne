from django.shortcuts import render, redirect
from . import models as m
from apps.auth_user.models import User
from apps.auth_user.views import is_blank
from django.contrib import messages
from django.db.models import Q

def index(request):
    quotes = m.Quote.objects.all().order_by('-created_at')

    context = {
        'quotes' : quotes
    }

    return render(request, 'litle_quote/index.html', context)

def quote_by_user(request, user_id):
    
    user = User.objects.get(id=user_id)
    quotes = m.Quote.objects.filter(user_id=user_id)

    context = {
        'user' : user.name,
        'quotes' : quotes
    }
    
    return render(request, 'litle_quote/quote.html', context)

def create_quote(request):
    if 'user_id' in request.session:

        if request.method == 'POST':

            content = request.POST['html_content']

            is_valid = True

            is_valid = not is_blank(request, 'content', content)

            if is_valid:

                try:
                    quote = m.Quote()
                    quote.content = content
                    quote.user_id = request.session['user_id']
                    quote.save()
                except:
                    messages.error(request, 'Save quote error!!')
            
        return redirect('litle_quote:index')

    return redirect('user_auth:index')

def edit_quote(request, quote_id):

    if 'user_id' in request.session:

        quote = m.Quote.objects.get(id=quote_id)

        context = {
            'quote' : quote
        }

        if request.method == 'POST':

            try:
                quote.content = request.POST['html_content']
                quote.save()
                return redirect('litle_quote:index')
            except:
                messages.error(request, 'Quote update error')
                return render(request, 'litle_quote/edit_quote.html', quote_id=quote_id)
        
        return render(request, 'litle_quote/edit_quote.html', context)

    return redirect('auth_user:index')

def delete_quote(request, quote_id):

    if 'user_id' in request.session:

        quote = m.Quote.objects.get(id=quote_id)
        quote.delete()
        
        return redirect('litle_quote:index')

    return redirect('auth_user:index')

def search_by_user_or_email(request):

    if request.method == 'POST':

        return redirect('litle_quote:results', query=request.POST['html_query'])

    return redirect('litle_quote:index')

def results(request, query):

    results = User.objects.filter(Q(name__icontains=query) | Q(email__icontains=query)).all()

    context = {
        'query' : query,
        'results' : results
    }

    return render(request, 'litle_quote/search.html', context)
