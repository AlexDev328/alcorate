from django.shortcuts import render
from .models import Drink

def drink_list(request):
    drinks = Drink.objects.order_by('alcohole')
    return render(request, 'boozing/drink_list.html', {'drinks': drinks})
