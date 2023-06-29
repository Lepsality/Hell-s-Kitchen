from django.contrib import admin
from .models import Reservation, Menu, Size, Price, PizzaRestaurant


class PriceInline(admin.TabularInline):
    model = Price
    extra = 1


class MenuAdmin(admin.ModelAdmin):
    inlines = [PriceInline]


admin.site.register(Reservation)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Size)
admin.site.register(Price)
admin.site.register(PizzaRestaurant)