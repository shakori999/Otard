# Generated by Django 4.0.3 on 2023-05-19 08:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0003_productinventory_is_on_sale'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('ordered_date', models.DateTimeField()),
                ('ordered', models.BooleanField(default=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(max_length=11, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('address_2', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('items', models.ManyToManyField(to='order.orderitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddIndex(
            model_name='order',
            index=models.Index(fields=['id'], name='id_order'),
        ),
    ]
