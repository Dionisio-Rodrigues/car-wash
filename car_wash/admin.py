from django.contrib import admin
from car_wash.models import *

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cpf', 'contact',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Cliente, ClienteAdmin)

class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'plate', 'owner',)
    list_display_links = ('id', 'model', 'plate')
    search_fields = ('model', 'plate')
    list_per_page = 20

admin.site.register(Car, CarAdmin)

class CheckinAdmin(admin.ModelAdmin):
    list_display = ('id', 'in_date', 'car')
    list_display_links = ('in_date', 'car',)
    search_fields = ('in_date', 'car',)
    list_per_page = 20

admin.site.register(Checkin, CheckinAdmin)

class CheckoutAdmin(admin.ModelAdmin):
    list_display = ('id', 'out_date', 'car')
    list_display_links = ('out_date', 'car',)
    search_fields = ('out_date', 'car',)
    list_per_page = 20

admin.site.register(Checkout, CheckoutAdmin)
