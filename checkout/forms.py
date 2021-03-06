from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    amount_pledged = forms.DecimalField(initial=1, min_value=1, label='Amount ($)')

    class Meta:
        model = Order
        fields = (
            'full_name',
            'email',
            'phone_number',
            'country',
            'postcode',
            'town_or_city',
            'street_address1',
            'street_address2',
            'county',
            'reward',
            'amount_pledged'
        )

        labels = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
            'reward': 'Choose the reward matching the amount you want to pledge',
            'amount_pledged': 'Amount ($)'
        }
