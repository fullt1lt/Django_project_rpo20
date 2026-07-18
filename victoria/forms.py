from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

from .models import Product

class MyForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class" : "input_email",
        "id" : "qwerty",
        "placeholder": "EMAIL"
    }))
    password = forms.CharField()

    def clean_password(self):
        password = self.cleaned_data["password"]
        if len(password) < 8:
            raise ValidationError("Длинна должна быть больше 8 символов!")
        return password

    def clean_email(self):
        email = self.cleaned_data["email"]
        if "gmail.com" in email:
            raise ValidationError("Емаил не может быть от гугла!!!")
        return email


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class LoginForm(forms.Form):
    username = forms.CharField(label="Логин")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            self.user = authenticate(username=username, password=password)
            if self.user is None:
                raise forms.ValidationError("Неверный логин или пароль")
        return cleaned_data
