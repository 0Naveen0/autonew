# Generated by Django 4.2.12 on 2024-07-01 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_alter_taxation_tax_end_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taxation',
            name='tax_end_date',
        ),
    ]