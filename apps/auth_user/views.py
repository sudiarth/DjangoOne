import re, bcrypt
from django.shortcuts import render, redirect
from . import models as m
from django.contrib import messages

EMAIL_REGEX = re.compile(r'^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$')

def index(request):
    return render(request, 'auth_user/index.html')

def is_blank(request, name, field):
    if len(field) == 0:
        messages.error(request, '{} Cannot be blank'.format(name))
        return True
    return False

def signup(request):

    name = request.POST['html_name']
    email = request.POST['html_email']
    password = request.POST['html_password']
    confirm = request.POST['html_confirm']

    is_valid = True

    is_valid = not is_blank(request, 'name', name)
    is_valid = not is_blank(request, 'email', email)
    is_valid = not is_blank(request, 'password', password)
    is_valid = not is_blank(request, 'confirm', confirm)

    if password != confirm:
        messages.error(request, 'password not match')
        is_valid = False
    if len(password) < 6:
        messages.error(request, 'pass to short')
    if not EMAIL_REGEX.match(email):
        messages.error(request, 'email format error')
    
    if is_valid:
        try:
            user = m.User()
            user.name = name
            user.email = email
            user.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            user.save()

            request.session['user_id'] = user.id
            request.session['name'] = user.name

            return redirect('project_manager:index')
        except:
            messages.error(request, 'email already registered dude')
    
    return redirect('auth_user:index')

def signin(request):
    email = request.POST['html_email']
    password = request.POST['html_password']

    try:
        user = m.User.objects.get(email=email)
        
        if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            request.session['user_id'] = user.id
            request.session['name'] = user.name
            return redirect('project_manager:index')
        else:
            messages.error(request, 'Password not match')
    except:
        messages.error(request, 'Invalid login')

    return redirect('auth_user:index')

def signout(request):
    request.session.clear()
    return redirect('base_html:index')