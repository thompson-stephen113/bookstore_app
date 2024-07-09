# Generated by Django 4.2.13 on 2024-07-02 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_type',
            field=models.CharField(choices=[('Hard cover', 'Hard cover'), ('E-book', 'E-Book'), ('Audiobook', 'Audiobook')], default='Hard cover', max_length=12),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('Classic', 'Classic'), ('Romantic', 'Romantic'), ('Comic', 'Comic'), ('Fantasy', 'Fantasy'), ('Horror', 'Horror'), ('Educational', 'Educational')], default='Classic', max_length=12),
        ),
    ]
