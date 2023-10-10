from django import forms
from base_app.models import Customer


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
        ]
