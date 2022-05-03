from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class CadastroForm(forms.ModelForm):

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name.upper()

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        return last_name.upper()

    def clean_email(self):
        email = self.cleaned_data['email']
        return email.lower()

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('Nome de usuário já ultilizado.')
        return username.lower()

    def clean(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']

        if password != password2:
            self.add_error('password', ValidationError('As senhas são diferentes.'))
            self.add_error('password2', ValidationError('As senhas são diferentes.'))

        return self.cleaned_data

    class Meta:
        model = User
        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome', 'required': True}),
            "last_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sobrenome', 'required': True}),
            "email": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'nome@exemplo.com', 'required': True}),
            "username": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuário', 'required': True}),
            "password": forms.PasswordInput(attrs={'class': 'form-control', 'required': True}),
            "password2": forms.PasswordInput(attrs={'class': 'form-control', 'required': True})
        }

        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "password",
            "password2",
        ]

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
