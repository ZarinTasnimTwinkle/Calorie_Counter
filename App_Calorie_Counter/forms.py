from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

class UserForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2']

class AuthForm(AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = UserEditModel
        fields = ['age', 'gender', 'height', 'weight']

class FoodEntryForm(forms.ModelForm):
    class Meta:
        model = FoodEntryModel
        fields = ['item_name', 'calories']