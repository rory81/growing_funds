from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('user','order_number', 'date','project_number','reward','amount_pledged' )
    fields = (
            'user',
            'order_number', 
            'full_name', 
            'email', 
            'phone_number', 
            'country',
            'postcode', 
            'town_or_city', 
            'street_address1', 
            'street_address2', 
            'county',
            'date',
            'project_number',
            'reward',
            'amount_pledged' 
        )
    list_display = (
            'user',
            'order_number', 
            'date',
            'project_number',
            'reward',
            'amount_pledged' 
        )
    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)