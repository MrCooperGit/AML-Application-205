# Generated by Django 4.0.6 on 2023-10-19 04:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('landing_app', '0003_alter_usertab_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertab',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
