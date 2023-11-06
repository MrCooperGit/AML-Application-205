from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import UserProfile, Entity, CustomUser


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'userType', 'entity')

    def clean_username(self):
        # Override the clean_username method to return the email as the username
        return self.cleaned_data['email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    userType = forms.ChoiceField(
        choices=[('', 'Select Company Type')] + UserProfile.USER_TYPE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'validationUserType',
            'required': True,
        }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'validationEmail',
        'required': True,
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'validationPassword1',
        'required': True,
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'validationPassword2',
        'required': True,
    }))
    entity = forms.ModelChoiceField(
        queryset=Entity.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'validationEntity',
            'required': True,
        }))


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'password1', 'password2',
                  'first_name', 'last_name', 'entity',)

        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': ''}),
            'password2': forms.PasswordInput(attrs={'class': 'form-outline flex-fill mb-0'}),
        }

    def __init__(self, entity, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['entity'].initial = entity
