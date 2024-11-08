from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50, label='Nombre de usuario', required=True)
    first_name = forms.CharField(max_length=50, label='Nombre', required=True)
    last_name = forms.CharField(max_length=50, label='Apellidos')
    email = forms.EmailField(max_length=100, label='Email', required=True)

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


    