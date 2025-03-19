from django import forms
from petrosa_energia_app.models import *
from django_countries.widgets import CountrySelectWidget


class ProductInterestForm(forms.ModelForm):
    class Meta:
        model = ProductInterest
        fields = ['name', 'email', 'address','company_name','phone_number','message', 'product',]
        widgets = {
            'product': forms.HiddenInput(),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter your address'}),
            'company_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Company Name'}),
            'phone_number': forms.NumberInput(attrs={'class' : 'form-control', 'placeholder': 'Your Phone Number'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        product = kwargs.pop('product', None)  # Pop product from kwargs to avoid the unexpected keyword argument error
        super().__init__(*args, **kwargs)
        if product:
            self.fields['product'].initial = product



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'subject', 'message']



class QuickQuoteForm(forms.ModelForm):
    class Meta:
        model = QuickQuote
        fields = ['product', 'first_name', 'last_name', 'email', 'company', 'company_address', 'phone', 'message']

        widgets = {
            'product': forms.HiddenInput(),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
            'company_address':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super(QuickQuoteForm, self).__init__(*args, **kwargs)
        if 'instance' in kwargs:
            self.fields['product'].initial = kwargs['instance'].product.name 