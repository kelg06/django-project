# Generated by Django 5.1.2 on 2024-11-19 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_entry_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='topic',
        ),
    ]
