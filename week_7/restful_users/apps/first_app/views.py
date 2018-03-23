# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'first_app/index.html', context)

def new_user(request):
    return render(request, 'first_app/new_user.html')

def create_user(request):
    User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email']
    )
    return redirect('/users')

def edit_user(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'first_app/edit_user.html', context)

def update_user(request, user_id):
    user_to_update = User.objects.get(id=user_id)
    user_to_update.first_name = request.POST['first_name']
    user_to_update.last_name = request.POST['last_name']
    user_to_update.email = request.POST['email']
    user_to_update.save()
    return redirect('/users')

def show_user(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'first_app/show_user.html', context)

def destroy_user(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/users')