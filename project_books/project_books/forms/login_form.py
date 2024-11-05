from django import forms 

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='Nombre de usuario', required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(),
        max_length=50, 
        label='Contraseña', 
        required=True)

