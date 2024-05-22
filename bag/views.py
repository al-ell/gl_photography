from django.shortcuts import render, redirect

from shop.views import *


def bag(request):
    """ Bag view """
    
    return render(request, 'bag/bag.html')


def add_to_bag(request, prints_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if prints_id in list(bag.keys()):
        bag[prints_id] += quantity
    else:
        bag[prints_id] = quantity
    
    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
