# Generated by Django 4.0.6 on 2023-10-16 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0010_rename_url_active_session_open_app'),
    ]

    operations = [
        migrations.CreateModel(
            name='Available_Apps',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
