# Generated by Django 4.0.3 on 2023-06-08 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_address_address_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_latitude',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_longitude',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_street',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
