from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=64)
    desc = models.CharField(max_length=500)


class Item(models.Model):
    name = models.CharField(max_length=50)  # nazwa produktu
    image_one = models.ImageField(upload_to="media", null=True, blank=True)
    image_two = models.ImageField(upload_to="media", null=True, blank=True)
    image_three = models.ImageField(upload_to="media", null=True, blank=True)
    desc = models.CharField(max_length=2000)  # opis produktu
    total_units = models.IntegerField()  # wszystkie sztuki
    sold_units = models.IntegerField(default=0)  # sprzedane sztuki
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # kategoria
    id = models.BigAutoField(primary_key=True)  # id produktu
    highlighted = models.BooleanField(default=False)  # czy item ma byc pokazywany na glownej stronie w ofertach

    stripe_product_id = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Price(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    stripe_price_id = models.CharField(max_length=100)
    price = models.IntegerField(default=0)  # cents

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)


class Order(models.Model):
    bought_item = models.ForeignKey(Item, on_delete=models.CASCADE)  # nazwa
    address = models.CharField(max_length=2000)  # adres
    customer_details = models.CharField(max_length=2000)  # dane uzytkownika, kontaktowe
    email = models.EmailField()  # email uzytkownika
    units = models.IntegerField()  # ilosc zamowionych sztuk
    total_price = models.IntegerField()  # pelna cena zamowienia
    order_id = models.BigAutoField(primary_key=True)  # id zamowienia
