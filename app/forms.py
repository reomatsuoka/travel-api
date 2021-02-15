from django import forms

class SearchForm(forms.Form):
    area = forms.CharField(label='地域', max_length=200, required=True)
