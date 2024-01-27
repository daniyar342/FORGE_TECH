from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib import admin
from .models import Apartment,City,Client


admin.site.unregister(Group)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name','number','status',]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display= ['name',]


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('id',"num_apartment", "location", "floor", "square", "date", "price", "status")
    list_filter = ("price", "num_apartment","floor","square", "status")
    search_fields = ['location__name',"price", "num_apartment","floor","square", "status"]