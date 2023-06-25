# Generated by Django 4.0.3 on 2023-06-12 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_address_address_city_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='address_city',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='address_street',
            new_name='addressCoustemId',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='address_name',
            new_name='addressType',
        ),
        migrations.AddField(
            model_name='address',
            name='contacktPersonNumer',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='address',
            name='contactPersonName',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
