from re import M
from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django.contrib.auth import get_user_model

PAYMENT_CHOICES = (
    ('S', 'Basra'),
)
user = get_user_model()
class CheckoutForm(forms.Form):
    name = forms.CharField(max_length=100)
    number = forms.CharField(max_length=11)
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '1234 Main st'
    }))
    apartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Apartment or suite'
    }))
    state = forms.ChoiceField(choices=PAYMENT_CHOICES)
    save_info = forms.BooleanField(required=False)
