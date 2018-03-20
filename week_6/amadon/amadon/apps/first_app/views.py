# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from products import items
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if "last_transaction" in request.session.keys():
        del request.session['last_transaction']

    context = {
        "items": items
    }
    return render(request, 'first_app/index.html', context)

def buy(request, item_id):
    for item in items:
        if item['id'] == int(item_id):
            amount_charged = item['price'] * int(request.POST['quantity'])

    try:
        request.session['total_charged']
    except KeyError:
        request.session['total_charged'] = 0

    try:
        request.session['total_items']
    except KeyError:
        request.session['total_items'] = 0

    request.session['total_charged'] += amount_charged
    request.session['total_items'] += int(request.POST['quantity'])
    request.session['last_transaction'] = amount_charged
    
    return redirect('/checkout')

def checkout(request):
    return render(request, 'first_app/checkout.html')