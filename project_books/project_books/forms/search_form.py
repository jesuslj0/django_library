from django import forms

# clase de formulario

class SearchForm(forms.Form):
    q = forms.CharField(
        label='Introduzca su busqueda',
        max_length=100,
    )