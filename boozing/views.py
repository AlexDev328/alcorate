from django.shortcuts import render
from .models import Drink

def drink_list(request):
    drinks = Drink.objects.order_by('alcohole')#.select_related('drink_type')
    return render(request, 'boozing/drink_list.html', {'drinks': drinks})
def drink(request, pk):
    print(pk)

    drink = Drink.objects.get(pk=pk)
    return render(request, 'boozing/drink.html', {'drink': drink})