from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Drink, DrinkType
from .forms import DrinkForm, DrinkTypeForm, DegustationForm, PurchaseForm
from django.views.generic import ListView, DetailView

def drink_list(request):
    drinks = Drink.objects.order_by('alcohole')#.select_related('drink_type')
    return render(request, 'boozing/drink_list.html', {'drinks': drinks})
def drink(request, pk):
    print(pk)

    drink = Drink.objects.get(pk=pk)
    return render(request, 'boozing/drink.html', {'drink': drink})

def create_drink(request):
    if request.method == 'POST':
        print(request.POST)
        drink_form = DrinkForm(request.POST)
        drink = drink_form.save()
        return redirect(f'{drink.id}/')

    else:
        forms = DrinkForm()
        return render(request, 'boozing/create_drink.html', {'form': forms})

def create_drink_type(request):
    if request.method == 'POST':
        drink_type_form = DrinkTypeForm(request.POST)
        drink_type = drink_type_form.save()
        return HttpResponse(content='Тип напитка добавлен', status=201)
    else:
        forms = DrinkTypeForm()
        return render(request, 'boozing/create_drink.html', {'form': forms})

def create_degustation(request):
    if request.method == 'POST':
        degustation_form = DegustationForm(request.POST)
        degustation = degustation_form.save()
        return HttpResponse(content='Дегустация добавлена ', status=201)
    else:
        forms = DegustationForm()
        return render(request, 'boozing/create_degustation.html', {'form': forms})

def create_purchase(request):
    if request.method == 'POST':
        purchase_form = PurchaseForm(request.POST)
        purchase = purchase_form.save()
        return HttpResponse(content='Покупка добавлена', status=201)
    else:
        forms = PurchaseForm()
        return render(request, 'boozing/create_purchase.html', {'form': forms})


class DrinkTypeTView(ListView):
    queryset = DrinkType.objects.all()
    template_name = 'boozing/drink_type_list.html'


class DrinkTypeDetailTView(DetailView):
    template_name = 'boozing/drink_type_list.html'

    def get_object(self, queryset=None):
        DrinkType.objects.get(pk=self.request.GET['pk'])



def test(request):
    return render(request, 'boozing/raiting.html')






