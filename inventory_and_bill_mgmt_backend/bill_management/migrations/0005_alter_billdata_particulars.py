# Generated by Django 4.1.5 on 2023-02-09 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bill_management', '0004_transaction_delete_monthlysummary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billdata',
            name='particulars',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bill_management.transaction'),
        ),
    ]