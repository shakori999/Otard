# Generated by Django 4.0.3 on 2023-05-19 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_productinventory_sale_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinventory',
            name='is_on_sale',
            field=models.BooleanField(default=False),
        ),
    ]
