from django import forms

# clase de formulario

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Nombre',
        max_length=60,
        required=True
    )
    email = forms.EmailField(
        label='Email',
        max_length=60,
        required=True
    )
    subject = forms.CharField(
        label='Motivo del contacto',
        max_length=60,
        required=True
    )
    coment = forms.CharField(
        max_length=200, 
        label='Coméntanos',
        widget=forms.Textarea
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if '@' not in email:
            raise forms.ValidationError('El email no tiene el formato correcto')
        return email
