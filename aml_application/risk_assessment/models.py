from django.db import models
from base_app.models import Entity


class RiskAssessment(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)

    offer_anonymity = models.BooleanField(default=False,
                                          verbose_name='Do you or your clients offer anonymity to customers?')

    offer_large_value_services = models.BooleanField(default=False,
                                                     verbose_name='Do you or your clients offer services for the movement of large values or volumes of funds?')

    offer_services_black_list = models.BooleanField(
        default=False, verbose_name='Do you or your clients offer services to any of the following countries? \nNorth Korea, Iran or Myanmar')
    offer_services_grey_list = models.BooleanField(
        default=False, verbose_name='Do you or your clients offer services to any of the following countries? \nAlbania, Barbados, Burkina Faso,'
        'Cameroon, Cayman Islands, Croatia, Democratic Republic of Congo, Gibraltar, Haiti, Jamaica, Jordan, Mali, Mozambique, Nigeria, Panama,'
        'Philippines, Senegal, South Africa, South Sudan, Syria, Tanzania, Türkiye, Uganda, UAE, Uganda, Vietnam or Yemen')
    offer_services_outside_NZ = models.BooleanField(default=False,
                                                    verbose_name='Do you or your clients offer services to customers outside New Zealand?')

    cash_intensive = models.BooleanField(default=False,
                                         verbose_name="Are yours or any of your client's services cash intensive?")
    company_services = models.BooleanField(default=False,
                                           verbose_name='Do you or your clients offer services for registering companies?')
    trust_services = models.BooleanField(default=False,
                                         verbose_name='Do you or your clients offer trust services?')
    remittance_services = models.BooleanField(default=False,
                                              verbose_name='Do you or your clients offer services for money remittance?')
    virtual_assets_services = models.BooleanField(default=False,
                                                  verbose_name='Do you or your clients offer services involving virtual/digital assets?')

    def __str__(self):
        return f"Risk Assessment for {self.date}"
