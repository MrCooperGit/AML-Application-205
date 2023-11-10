from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import UserProfile, Entity, CustomUser


class CustomLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',
                  'userType', 'entity',)

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

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'password1', 'password2',
                  'first_name', 'last_name', 'entity',)

    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    entity = forms.ModelChoiceField(
        queryset=Entity.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email
