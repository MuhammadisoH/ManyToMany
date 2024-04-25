from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django import forms

from .models import Student

User = get_user_model()


class UserRegistrationForm(ModelForm):
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'hobbies']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full border rounded border-gray-900 py-2 px-4 outline-0'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full border rounded border-gray-900 py-2 px-4 outline-0'
            }),
            # 'hobbies': forms.Sele(attrs={
            #     'class': 'w-full border rounded border-gray-900 py-2 px-4 outline-0'
            # }),
        }
