# Generated by Django 5.1.4 on 2025-01-16 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_book_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('available', 'Available'), ('sold', 'sold'), ('rented', 'rented')], default='available', max_length=50),
        ),
    ]
