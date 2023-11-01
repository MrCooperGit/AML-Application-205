from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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
                  'entity', 'first_name', 'last_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
