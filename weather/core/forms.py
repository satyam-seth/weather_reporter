from django import forms

class SearchForm(forms.Form):
    loc=forms.CharField()