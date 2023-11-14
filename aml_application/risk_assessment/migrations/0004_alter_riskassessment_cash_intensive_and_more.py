# Generated by Django 4.0.6 on 2023-11-12 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_assessment', '0003_alter_riskassessment_cash_intensive_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riskassessment',
            name='cash_intensive',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='company_services',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='offer_anonymity',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='offer_large_value_services',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='offer_services_black_list',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='offer_services_grey_list',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='offer_services_outside_NZ',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='remittance_services',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='trust_services',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='virtual_assets_services',
            field=models.CharField(max_length=20),
        ),
    ]
