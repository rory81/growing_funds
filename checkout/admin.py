from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('user_profile', 'order_number', 'date','project','reward','amount_pledged')
    fields = (
            'user_profile',
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
            'project',
            'reward',
            'amount_pledged',
        )
    list_display = (
        'user_profile',
        'order_number',
        'date',
        'project',
        'reward',
        'amount_pledged',
        )
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
