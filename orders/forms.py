from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email',
                  'address', 'postal_code', 'city']
        labels = {
            'first_name': '',  # an empty string for labels to avoid fieldnames getting rendered on the bootstrap fields
            'last_name': '',
            'email': '',
            'address': '',
            'postal_code': '',
            'city': '',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'FIRST NAME'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'LAST NAME'}),
            'city': forms.TextInput(attrs={'placeholder': 'COUNTRY'}),
            'email': forms.TextInput(attrs={'placeholder': 'EMAIL ADDRESS'}),
            'address': forms.TextInput(attrs={'placeholder': 'ADDRESS'}),
            'postal_code': forms.TextInput(attrs={'placeholder': 'ZIP CODE'})
        }