# views.py
from __future__ import unicode_literals
import random
import string
from django.shortcuts import render, redirect

def first_app(n):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))

# Create your views here.
def index(request):
    try:
        request.session['count']
    except KeyError:
        request.session['count'] = 0

    return render(request, "index.html")

def generate(request):
    request.session['count'] += 1  
    request.session['random_word'] = first_app(10)
    return redirect('/')

def reset(request):
    del request.session['count']
    del request.session['random_word']
    return redirect('/')