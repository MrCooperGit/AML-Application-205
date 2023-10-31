# Generated by Django 4.0.6 on 2023-10-18 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base_app', '0014_delete_active_session'),
    ]

    operations = [
        migrations.CreateModel(
            name='Active_Session',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_app.entity')),
            ],
        ),
        migrations.CreateModel(
            name='UserTab',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=False)),
                ('app_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_app.availableapps')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing_app.active_session')),
            ],
        ),
    ]