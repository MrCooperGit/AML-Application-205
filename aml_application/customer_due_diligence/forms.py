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
    date_of_birth = forms.DateField(),
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
    existing_customers = forms.ModelChoiceField(
        queryset=Customer.objects.none(),
        required=False,
    )

    class Meta:
        model = Customer
        fields = [
            'existing_customers',
            'proof_of_address',
            'proof_of_identity',
        ]

    def __init__(self, *args, **kwargs):
        existing_customers = kwargs.pop('existing_customers', None)
        super().__init__(*args, **kwargs)

        if existing_customers is not None:
            self.fields['existing_customers'].queryset = existing_customers
