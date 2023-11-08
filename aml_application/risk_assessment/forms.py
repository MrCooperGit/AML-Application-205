from django import forms
from .models import RiskAssessment

YES_NO_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)


class RiskAssessmentForm(forms.ModelForm):
    offer_anonymity = forms.ChoiceField(
        label=RiskAssessment._meta.get_field('offer_anonymity').verbose_name,
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-inline'}),
    )
    offer_large_value_services = forms.BooleanField(
        label=RiskAssessment._meta.get_field(
            'offer_large_value_services').verbose_name,
        widget=forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')], attrs={
            'class': 'form-check-inline'}),
    )
    offer_services_black_list = forms.BooleanField(
        label=RiskAssessment._meta.get_field(
            'offer_services_black_list').verbose_name,
        widget=forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')], attrs={
            'class': 'form-check-inline'}),
    )
    offer_services_grey_list = forms.BooleanField(
        label=RiskAssessment._meta.get_field(
            'offer_services_grey_list').verbose_name,
        widget=forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')], attrs={
            'class': 'form-check-inline'}),
    )
    offer_services_outside_NZ = forms.BooleanField(
        label=RiskAssessment._meta.get_field(
            'offer_services_outside_NZ').verbose_name,
        widget=forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')], attrs={
            'class': 'form-check-inline'}),
    )
    cash_intensive = forms.BooleanField(
        label=RiskAssessment._meta.get_field('cash_intensive').verbose_name,
        widget=forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')], attrs={
            'class': 'form-check-inline'}),
    )
    company_services = forms.BooleanField(
        label=RiskAssessment._meta.get_field('company_services').verbose_name,
        widget=forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')], attrs={
            'class': 'form-check-inline'}),
    )
    trust_services = forms.BooleanField(
        label=RiskAssessment._meta.get_field('trust_services').verbose_name,
        widget=forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')], attrs={
            'class': 'form-check-inline'}),
    )
    remittance_services = forms.BooleanField(
        label=RiskAssessment._meta.get_field(
            'remittance_services').verbose_name,
        widget=forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')], attrs={
            'class': 'form-check-inline'}),
    )
    virtual_assets_services = forms.BooleanField(
        label=RiskAssessment._meta.get_field(
            'virtual_assets_services').verbose_name,
        widget=forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')], attrs={
            'type': 'checkbox', 'class': 'form-check-inline'}),
    )

    class Meta:
        model = RiskAssessment
        fields = '__all__'
        exclude = ['entity']
