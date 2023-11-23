from django.db import models
from base_app.models import Entity


class RiskAssessment(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    offer_anonymity = models.CharField(max_length=20)
    offer_large_value_services = models.CharField(max_length=20)
    offer_services_black_list = models.CharField(max_length=20)
    offer_services_grey_list = models.CharField(max_length=20)
    offer_services_outside_NZ = models.CharField(max_length=20)
    cash_intensive = models.CharField(max_length=20)
    company_services = models.CharField(max_length=20)
    trust_services = models.CharField(max_length=20)
    remittance_services = models.CharField(max_length=20)
    virtual_assets_services = models.CharField(max_length=20)

    def __str__(self):
        return f"Risk Assessment for {self.date_created}"
