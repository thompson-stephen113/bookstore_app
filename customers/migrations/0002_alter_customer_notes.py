# Generated by Django 4.2.13 on 2024-06-25 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='notes',
            field=models.TextField(default='no notes...'),
        ),
    ]