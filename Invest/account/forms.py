from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Item
from django.core.validators import validate_email

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


class SignupForm(UserCreationForm):
    """
        Форма для регистрацию через почту
    """
    name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(max_length=200, help_text='Ваша почта', required=True)
    phone = forms.CharField(max_length=100, required=True)
    interest = forms.ChoiceField(
        label='Меня больше интересует',
        widget=forms.RadioSelect,
        choices=[('investing', 'Инвестиции'),
                 ('project', 'Привлечение денег в свои проекты')]
    )
    

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) == 0:
            raise 

    class Meta:
        """
            Конфигурация формы
        """
        model = User
        fields = ('email','name', 'password1', 'password2')

