# Generated by Django 4.1.7 on 2023-02-19 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('thumbnail', models.CharField(max_length=255, unique=True)),
                ('main_image', models.CharField(max_length=255, unique=True)),
                ('description', models.CharField(max_length=512)),
                ('content', models.JSONField()),
            ],
        ),
    ]
