# Generated by Django 4.0.6 on 2023-11-06 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_assessment', '0002_riskassessment_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riskassessment',
            name='cash_intensive',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], verbose_name="Are yours or any of your client's services cash intensive?"),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='company_services',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], verbose_name='Do you or your clients offer services for registering companies?'),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='offer_anonymity',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], verbose_name='Do you or your clients offer anonymity to customers?'),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='offer_large_value_services',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], verbose_name='Do you or your clients offer services for the movement of large values or volumes of funds?'),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='offer_services_black_list',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], verbose_name='Do you or your clients offer services to any of the following countries? \nNorth Korea, Iran or Myanmar'),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='offer_services_grey_list',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], verbose_name='Do you or your clients offer services to any of the following countries? \nAlbania, Barbados, Burkina Faso,Cameroon, Cayman Islands, Croatia, Democratic Republic of Congo, Gibraltar, Haiti, Jamaica, Jordan, Mali, Mozambique, Nigeria, Panama,Philippines, Senegal, South Africa, South Sudan, Syria, Tanzania, Türkiye, Uganda, UAE, Uganda, Vietnam or Yemen'),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='offer_services_outside_NZ',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], verbose_name='Do you or your clients offer services to customers outside New Zealand?'),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='remittance_services',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], verbose_name='Do you or your clients offer services for money remittance?'),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='trust_services',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], verbose_name='Do you or your clients offer trust services?'),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='virtual_assets_services',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], verbose_name='Do you or your clients offer services involving virtual/digital assets?'),
        ),
    ]
