from django import forms
from .models import Product



class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields=['Productimage','name']
		label={'Productimage':'pi', 'name':'Name'}
		widegets={'pi':forms.ImageField(),'Name':forms.CharField(),}