# Generated by Django 4.2.13 on 2024-07-02 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salespersons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesperson',
            name='pic',
            field=models.ImageField(default='no_picture.jpg', upload_to='salespersons'),
        ),
    ]