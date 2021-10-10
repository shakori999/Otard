# Generated by Django 3.2.3 on 2021-10-10 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_productattribute_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productattribute',
            name='name',
            field=models.CharField(help_text='required', max_length=255, unique=True, verbose_name='attribute name'),
        ),
    ]