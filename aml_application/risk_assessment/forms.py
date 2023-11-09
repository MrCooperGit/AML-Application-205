from django import forms
from .models import RiskAssessment

YES_NO_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)


class RiskAssessmentForm(forms.ModelForm):
    offer_anonymity = forms.ChoiceField(
        label='Do you or your clients offer anonymity to customers?',
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-inline'}),
    )
    offer_large_value_services = forms.ChoiceField(
        label='Do you or your clients offer services for the movement of large values or volumes of funds?',
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect(attrs={
            'class': 'form-check-inline'}),
    )
    offer_services_black_list = forms.ChoiceField(
        label='Do you or your clients offer services to any of the following countries? \nNorth Korea, Iran or Myanmar',
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect(attrs={
            'class': 'form-check-inline'}),
    )
    offer_services_grey_list = forms.ChoiceField(
        label='Do you or your clients offer services to any of the following countries? \nAlbania, Barbados, Burkina Faso,'
        'Cameroon, Cayman Islands, Croatia, Democratic Republic of Congo, Gibraltar, Haiti, Jamaica, Jordan, Mali, Mozambique, Nigeria, Panama,'
        'Philippines, Senegal, South Africa, South Sudan, Syria, Tanzania, Türkiye, Uganda, UAE, Uganda, Vietnam or Yemen',
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect(attrs={
            'class': 'form-check-inline'}),
    )
    offer_services_outside_NZ = forms.ChoiceField(
        label='Do you or your clients offer services to customers outside New Zealand?',
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect(attrs={
            'class': 'form-check-inline'}),
    )
    cash_intensive = forms.ChoiceField(
        label="Are yours or any of your client's services cash intensive?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect(attrs={
            'class': 'form-check-inline'}),
    )
    company_services = forms.ChoiceField(
        label='Do you or your clients offer services for registering companies?',
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect(attrs={
            'class': 'form-check-inline'}),
    )
    trust_services = forms.ChoiceField(
        label='Do you or your clients offer trust services?',
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect(attrs={
            'class': 'form-check-inline'}),
    )
    remittance_services = forms.ChoiceField(
        label='Do you or your clients offer services for money remittance?',
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect(attrs={
            'class': 'form-check-inline'}),
    )
    virtual_assets_services = forms.ChoiceField(
        label='Do you or your clients offer services involving virtual/digital assets?',
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect(attrs={
            'type': 'checkbox', 'class': 'form-check-inline'}),
    )

    class Meta:
        model = RiskAssessment
        fields = '__all__'
        exclude = ['entity']
