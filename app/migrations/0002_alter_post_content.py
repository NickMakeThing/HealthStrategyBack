# Generated by Django 4.1.7 on 2023-02-19 12:19

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), size=None),
        ),
    ]
