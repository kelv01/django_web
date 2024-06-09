#forms

from django import forms 
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'drink_type', 'size', ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'name'}),
            'phone': forms.TextInput(attrs={'placeholder': 'phone'}),
            'drink_type': forms.Select(attrs={'id': 'drink-type'}),
            'size': forms.Select(attrs={'id': 'size'}),
        }