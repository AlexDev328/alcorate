from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class DrinkType(models.Model):
    name = models.CharField(max_length=12)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип напитка'
        verbose_name_plural = 'Тип напитков'


class Shop(models.Model):
    name = models.CharField(max_length=12)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Место покупки'
        verbose_name_plural = 'Место покупок'


class Drink(models.Model):
    name = models.CharField('Наименование напитка', max_length=50)
    alcohole = models.IntegerField('Процент спирта', validators=[MinValueValidator(0), MaxValueValidator(100)])
    volume = models.FloatField('объем')
    drink_type = models.ForeignKey(DrinkType, on_delete=models.DO_NOTHING, verbose_name='Тип напитка')

    @property
    def raiting(self):
        return 5

    @property
    def avg_price(self):
        return 10

    class Meta:
        verbose_name = 'Напиток'
        verbose_name_plural = 'Напитки'


class Degustation(models.Model):
    data = models.DateField(auto_now_add=True)
    drink = models.ForeignKey(Drink, on_delete=models.DO_NOTHING)
    like = models.BooleanField('Понравилось')

    def __str__(self):
        return self.drink, self.data

    class Meta:
        verbose_name = 'Дегустация'
        verbose_name_plural = 'Дегустации'


class Purchase(models.Model):
    price = models.DecimalField('Цена',max_digits=4, decimal_places=2)
    drink = models.ForeignKey(Drink, on_delete=models.DO_NOTHING, related_name='purchases')
    shop = models.ForeignKey(Shop, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.drink.name, self.shop, self.price

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'
