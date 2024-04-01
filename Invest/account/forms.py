from typing import Any
import phonenumbers

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Item
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


from .models import SupportMail

class SupportMailForm(forms.ModelForm):
    class Meta:
        model = SupportMail
        fields = ['name', 'email', 'message']


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'city',
                  'required_investment', 'profit_per_month', 'user', 'category']


class SignupForm(forms.ModelForm):
    """
        Форма для регистрацию через почту
    """
    username = forms.CharField(
        max_length=32,
        required=True,
        error_messages={
            "required": "Обязательное поле"
        }
    )
    email = forms.EmailField(
        max_length=50,
        required=True,
        error_messages={
            "required": "Обязательное поле"
        }
    )
    phone = forms.CharField(
        max_length=32,
        required=True,
        error_messages={
            "required": "Обязательное поле"
        }
    )
    interest = forms.ChoiceField(
        label='Меня больше интересует',
        required=True,
        widget=forms.RadioSelect,
        choices=[('investing', 'Инвестиции'),
                 ('project', 'Привлечение денег в свои проекты')]
    )
    password = forms.CharField(
        max_length=32,
        min_length=5,
        required=True,
        error_messages={
            "required": "Обязательное поле",
            "min_length": "Минимум 5 знаков",
        }
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            "required": "Обязательное поле",
            "placeholder": "Повторить пароль",
        })
    )
    
    
    class Meta:
        """
            Конфигурация формы
        """
        model = User
        fields = ("username", "email", "password")


    def clean_username(self):
        if not self.cleaned_data['username'].strip():
            raise forms.ValidationError("Обязательное поле")
        elif len(self.cleaned_data['username']) < 5:
            raise forms.ValidationError("Минимум 5 знаков")
        else:
            return self.cleaned_data['username']
        
    
    def clean_email(self):
        try:
            validate_email(self.cleaned_data["email"])
        except ValidationError:
            raise forms.ValidationError("Укажите корректную почту")
        if User.objects.filter(email=self.cleaned_data["email"]).exists():
            raise forms.ValidationError("Почта уже зарегистрирована")
        return self.cleaned_data["email"]
    
    
    def clean_phone(self):
        try:
            parse_phone = phonenumbers.parse(self.cleaned_data['phone'], None)
            if not phonenumbers.is_valid_number(parse_phone):
                raise ValidationError("Неверный номер телефона")
        except phonenumbers.phonenumberutil.NumberParseException:
            raise ValidationError("Неверный номер телефона")
        return self.cleaned_data['phone']
    

class SignIn(forms.ModelForm):
    email = forms.EmailField(
        max_length=50,
        required=True,
        error_messages={
            "required": "Обязательное поле"
        }
    )
    password = forms.CharField(
        max_length=32,
        min_length=5,
        required=True,
        error_messages={
            "required": "Обязательное поле",
            "min_length": "Минимум 5 знаков",
        }
    )

    class Meta:
        """
            Конфигурация формы
        """
        model = User
        fields = ("email", "password")

        
    
    
    