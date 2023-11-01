# Generated by Django 4.0.6 on 2023-10-24 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0009_alter_entity_options'),
        ('risk_assessment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='riskassessment',
            name='blacklisted_countries',
        ),
        migrations.RemoveField(
            model_name='riskassessment',
            name='blacklisted_countries_list',
        ),
        migrations.RemoveField(
            model_name='riskassessment',
            name='customer_service_types',
        ),
        migrations.RemoveField(
            model_name='riskassessment',
            name='customer_services',
        ),
        migrations.AddField(
            model_name='riskassessment',
            name='company_services',
            field=models.BooleanField(default=False, verbose_name='Do you or your clients offer services for registering companies?'),
        ),
        migrations.AddField(
            model_name='riskassessment',
            name='entity',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base_app.entity'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='riskassessment',
            name='offer_services_black_list',
            field=models.BooleanField(default=False, verbose_name='Do you or your clients offer services to any of the following countries? \nNorth Korea, Iran or Myanmar'),
        ),
        migrations.AddField(
            model_name='riskassessment',
            name='offer_services_grey_list',
            field=models.BooleanField(default=False, verbose_name='Do you or your clients offer services to any of the following countries? \nAlbania, Barbados, Burkina Faso,Cameroon, Cayman Islands, Croatia, Democratic Republic of Congo, Gibraltar, Haiti, Jamaica, Jordan, Mali, Mozambique, Nigeria, Panama,Philippines, Senegal, South Africa, South Sudan, Syria, Tanzania, Türkiye, Uganda, UAE, Uganda, Vietnam or Yemen'),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='cash_intensive',
            field=models.BooleanField(default=False, verbose_name="Are yours or any of your client's services cash intensive?"),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='offer_anonymity',
            field=models.BooleanField(default=False, verbose_name='Do you or your clients offer anonymity to customers?'),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='offer_large_value_services',
            field=models.BooleanField(default=False, verbose_name='Do you or your clients offer services for the movement of large values or volumes of funds?'),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='offer_services_outside_NZ',
            field=models.BooleanField(default=False, verbose_name='Do you or your clients offer services to customers outside New Zealand?'),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='remittance_services',
            field=models.BooleanField(default=False, verbose_name='Do you or your clients offer services for money remittance?'),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='trust_services',
            field=models.BooleanField(default=False, verbose_name='Do you or your clients offer trust services?'),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='virtual_assets_services',
            field=models.BooleanField(default=False, verbose_name='Do you or your clients offer services involving virtual/digital assets?'),
        ),
    ]
