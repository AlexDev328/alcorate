from django import forms

from .models import DrinkType, Drink, Shop, Degustation, Purchase


class DrinkForm(forms.ModelForm):

    class Meta:
        model = Drink
        fields = ('name', 'alcohole', 'volume', 'drink_type')


class DrinkTypeForm(forms.ModelForm):

    class Meta:
        model = DrinkType
        fields = ('name',)


class ShopForm(forms.ModelForm):

    class Meta:
        model = Shop
        fields = ('name', )


class DegustationForm(forms.ModelForm):

    class Meta:
        model = Degustation
        fields = ('drink', 'like')


class PurchaseForm(forms.ModelForm):

    class Meta:
        model = Purchase
        fields = ('price', 'drink', 'shop')