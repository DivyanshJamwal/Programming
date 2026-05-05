from django import forms

class MyForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Name')
    email = forms.EmailField(required=True, label='Email')
    message = forms.CharField(widget=forms.Textarea, required=True, label='Message')
    phone = forms.CharField(max_length=15, required=False, label='Phone')
