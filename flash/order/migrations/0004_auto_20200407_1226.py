# Generated by Django 2.2 on 2020-04-07 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20200407_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderedproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='order.Order'),
        ),
    ]
