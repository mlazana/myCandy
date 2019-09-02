from django import forms

class valueForm(forms.Form):
	moneyValue = forms.CharField(max_length=100)