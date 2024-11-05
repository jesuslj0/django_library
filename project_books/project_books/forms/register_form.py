from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label='Nombre de usuario', required=True)
    first_name = forms.CharField(max_length=50, label='Nombre', required=True)
    last_name = forms.CharField(max_length=50, label='Apellidos')
    email = forms.EmailField(max_length=100, label='Email', required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(),
        max_length=50, 
        label='Contraseña', 
        required=True)
    password_confirm= forms.CharField(
        widget=forms.PasswordInput(),
        max_length=50, 
        label='Confirme la contraseña', 
        required=True
    )

    def clean_password(self):
        password = self.cleaned_data.get('password')

        # Validar la contraseña usando Django's validate_password
        try:
            validate_password(password)
        except ValidationError as error:
            # Si hay errores de validación, los añadimos al formulario
            self.add_error('password', error)

        return password

    # Validar que las contraseñas coincidan
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise ValidationError("Las contraseñas no coinciden.")

    