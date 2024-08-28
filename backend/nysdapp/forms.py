from django import forms
from .models import Subscriber
from .models import CartItem

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']  
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email',
                'class': 'form-control',
                'required': True,
            }),
        }


class AddToCartForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={'min': '1', 'value': '1'}),
        }
