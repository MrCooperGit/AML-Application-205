# Generated by Django 4.0.6 on 2023-10-17 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0011_available_apps'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='available_apps',
            options={'ordering': ('name',), 'verbose_name_plural': 'Available Apps'},
        ),
    ]
