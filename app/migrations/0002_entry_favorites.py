# Generated by Django 5.1.2 on 2024-11-13 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='favorites',
            field=models.BooleanField(default=False),
        ),
    ]