from django import forms
from .models import ProductInterest



class ProductInterestForm(forms.ModelForm):
    class Meta:
        model = ProductInterest
        fields = ['name', 'email', 'message', 'product']
        widgets = {
            'product': forms.HiddenInput(),  # Product field is hidden and not editable
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        product = kwargs.pop('product', None)  # Pop product from kwargs to avoid the unexpected keyword argument error
        super().__init__(*args, **kwargs)
        if product:
            self.fields['product'].initial = product
