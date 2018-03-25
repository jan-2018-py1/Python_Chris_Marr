# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Course
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'first_app/index.html', context)

def create(request):
    Course.objects.create(
        name=request.POST['name'],
        description=request.POST['description']
    )
    return redirect('/')

def confirm(request, course_id):
    context = {
        "course": Course.objects.get(id=course_id)
    }
    return render(request, 'first_app/confirm.html', context)

def destroy(request, course_id):
    Course.objects.get(id=course_id).delete()
    return redirect('/')