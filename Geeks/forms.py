from django import forms

class GeeksForms(forms.Form):
    titel = forms.CharField()
    descriptsion = forms.CharField()