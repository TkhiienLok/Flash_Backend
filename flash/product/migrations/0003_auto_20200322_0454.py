# Generated by Django 2.2 on 2020-03-22 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200322_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Organization'),
        ),
    ]
