# Generated by Django 4.1.5 on 2023-02-09 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill_management', '0003_transactiontype_billdata_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('particular', models.CharField(max_length=50)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='MonthlySummary',
        ),
    ]
