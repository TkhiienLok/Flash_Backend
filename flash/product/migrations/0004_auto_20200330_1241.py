# Generated by Django 2.2 on 2020-03-30 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20200322_0454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='manager',
        ),
        migrations.AlterField(
            model_name='product',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.Organization'),
        ),
        migrations.DeleteModel(
            name='Filial',
        ),
        migrations.DeleteModel(
            name='Organization',
        ),
    ]