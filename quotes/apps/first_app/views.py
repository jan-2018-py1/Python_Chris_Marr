from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from .models import User
#from ..review.models import Book
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')

def register(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "You've successfully registered.")
    return HttpResponseRedirect(reverse("second_app:index"))

def login(request):
    result = User.objects.validate_login(request.POST)
    request.session['user_id'] = result.id
    messages.success(request, "You are now logged in.")
    return HttpResponseRedirect(reverse("second_app:index"))

def logout(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')

def success(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'first_app/success.html', context)

def show(request, user_id):
    user = User.objects.get(id=user_id)
    unique_ids = user.reviews_left.all().values("quote").distinct()
    quotes = []
    for quote in unique_ids:
        unique_quotes.append(quote.objects.get(id=quote['quote']))
    context = {
        'user': user,
        'quotes': quotes
    }
    return render(request, 'first_app/show.html', context)