from django import forms

class SearchForm(forms.Form):
    loc=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control shadow-lg','placeholder':'enter your location here'}))