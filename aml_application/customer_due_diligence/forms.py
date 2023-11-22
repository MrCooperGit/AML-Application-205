from django import forms
from base_app.models import Customer, Entity, Company
# from datetime import datetime

YES_NO_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)


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
            'entity', 'is_director', 'is_shareholder', 'company'
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
    is_director = forms.ChoiceField(choices=YES_NO_CHOICES,)
    is_shareholder = forms.ChoiceField(choices=YES_NO_CHOICES,)
    company = forms.ModelChoiceField(
        queryset=Company.objects.none(), required=False)

    def clean(self):
        cleaned_data = super().clean()
        is_director = cleaned_data.get('is_director')
        is_shareholder = cleaned_data.get('is_shareholder')
        company = cleaned_data.get('company')

        # Check that if the customer is a director or shareholder, a company is selected
        if (is_director == 'Yes' or is_shareholder == 'Yes') and not company:
            raise forms.ValidationError(
                'Please select a company for the director or shareholder.')

        return cleaned_data

    def __init__(self, *args, **kwargs):
        company_choices = kwargs.pop('company_choices', None)
        super().__init__(*args, **kwargs)

        if company_choices is not None:
            self.fields['company'].queryset = company_choices


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


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'company_registration_num', 'address', 'entity']

    entity = forms.ModelChoiceField(
        queryset=Entity.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'validationEntity',
            'required': True,
        }))

    widgets = {
        'company_registration_num': forms.TextInput(attrs={'maxlength': 20}),
    }
