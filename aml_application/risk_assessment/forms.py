from django import forms
from django.contrib.auth.decorators import login_required
from .models import RiskAssessment


class RiskAssessmentForm(forms.ModelForm):
    offer_anonymity = forms.BooleanField(
        label=RiskAssessment._meta.get_field('offer_anonymity').verbose_name,
        widget=forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')], attrs={
            'class': 'form-check-inline'}),
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

    # set the value of 'entity' to that of the logged in user
    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop('user', None)
    #     super(RiskAssessmentForm, self).__init__(*args, **kwargs)

    #     if user:
    #         self.fields['entity'].initial = user.entity.name
    #     else:
    #         print("No entity found for user")
