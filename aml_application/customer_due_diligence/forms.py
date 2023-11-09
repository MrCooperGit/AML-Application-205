from django import forms
from base_app.models import Customer, Entity
# from datetime import datetime


class CustomerDueDiligenceForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'full_name',
            'date_of_birth',
            'address',
            'phone',
            'email',
            'additional_info',
            'entity',
        ]

    full_name = forms.CharField(),
    date_of_birth = forms.DateField(input_formats=['dd-MM-yyyy']),
    address = forms.CharField(),
    phone = forms.IntegerField(),
    email = forms.EmailField(),
    additional_info = forms.CharField(),
    entity = forms.ModelChoiceField(
        queryset=Entity.objects.all(),
        empty_label=None,
        required=False
    )


class CustomerVerificationForm(forms.ModelForm):
    existing_customer = forms.ModelChoiceField(
        queryset=Customer.objects.all(),
        empty_label="Select an existing customer",
        required=True,
    )

    class Meta:
        model = Customer
        fields = [
            'existing_customer',
            'proof_of_address',
            'proof_of_identity',
        ]

        widgets = {
            'proof_of_address': forms.ClearableFileInput(attrs={'multiple': False}),
            'proof_of_identity': forms.ClearableFileInput(attrs={'multiple': False}),
        }
