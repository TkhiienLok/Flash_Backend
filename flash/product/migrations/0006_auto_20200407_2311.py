# Generated by Django 2.2 on 2020-04-07 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20200407_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.Organization'),
        ),
    ]
