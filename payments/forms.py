from django import forms
from .models import Fund
from projects.models import Project
from datetime import datetime
"""
Added required=False so that the plain text with creditcard details are not transmitted through the browser for privacy and security reasons
"""
class MakePaymentForm(forms.Form):
    MONTH_CHOICES = [(i,i) for i in range(1,13)]
    YEAR_CHOICES = [(i,i) for i in range(datetime.now().year,datetime.now().year+20)]

    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security Code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

class FundForm(forms.ModelForm):
    class Meta:
        model = Fund
        fields = ('full_name', 'phone_number','country', 'amount')

