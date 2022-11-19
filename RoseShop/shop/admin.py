from django.contrib import admin
from .models import Item, Order, Category, Price


# Register your models here.


class PriceInlineAdmin(admin.TabularInline):
    model = Price
    extra = 0


class ItemAdmin(admin.ModelAdmin):
    inlines = [PriceInlineAdmin]


admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
admin.site.register(Order)
