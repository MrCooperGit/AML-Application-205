# Generated by Django 4.0.6 on 2023-10-19 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_app', '0002_remove_usertab_session_usertab_user_alter_usertab_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertab',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]