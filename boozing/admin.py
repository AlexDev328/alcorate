from django.contrib import admin
from .models import Drink, DrinkType, Shop, Purchase, Degustation


# Register your models here.

@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'alcohole', 'volume','avg_price','raiting')
    fields = ( 'name', 'alcohole', 'volume','avg_price','raiting')
    readonly_fields = ('avg_price','raiting')


@admin.register(DrinkType)
class DrinkTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    pass


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    pass


@admin.register(Degustation)
class DegustationAdmin(admin.ModelAdmin):
    pass
