#creating forms for user info

from django import forms 
from .models import Order
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm



class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    phone_number = forms.CharField(max_length=50, help_text='Required')



    class Meta:

        model = User
        fields = ['username', 'email', 'password1',]



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




#forms

"""from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Order

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    phone_number = forms.CharField(max_length=50, help_text='Required')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'phone_number']


def save(self, commit=True):
    user = super(SignUpForm, self).save(commit=False)
    user.email = self.cleaned_data['email']
    user.phone_number = self.cleaned_data['phone_number']
    if commit:
        user.save()
    return user



class OrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ['product_name', 'quantity']


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number']
"""