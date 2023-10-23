from django.db import models


class RiskAssessment(models.Model):
    offer_anonymity = models.BooleanField(
        verbose_name='Do you offer anonymity to your customers?')
    offer_large_value_services = models.BooleanField(
        verbose_name='Do you offer services for the movement of large values and/or volumes of funds?')
    offer_services_outside_NZ = models.BooleanField(
        verbose_name='Are your services available to customers outside New Zealand?')
    blacklisted_countries = models.BooleanField(
        verbose_name='Do your customers offer services to blacklisted countries?')
    blacklisted_countries_list = models.TextField(
        verbose_name='If yes, please specify which countries.')
    cash_intensive = models.BooleanField(
        verbose_name='Are any of your customer’s services cash intensive?')
    customer_services = models.BooleanField(
        verbose_name='Do your customers offer services for specific company types?')
    customer_service_types = models.TextField(
        verbose_name='If yes, please specify which types of companies.')
    trust_services = models.BooleanField(
        verbose_name='Do your customers offer trust services?')
    remittance_services = models.BooleanField(
        verbose_name='Do you offer services for money remittance?')
    virtual_assets_services = models.BooleanField(
        verbose_name='Do you offer services involving virtual/digital assets?')

    def __str__(self):
        return f"Risk Assessment for {self.date}"
