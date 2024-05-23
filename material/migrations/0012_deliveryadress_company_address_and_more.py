# Generated by Django 4.2.5 on 2024-05-23 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0011_companyaddress_storelocation'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryadress',
            name='company_address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='material.companyaddress'),
        ),
        migrations.AlterField(
            model_name='deliveryadress',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='deliveryadress',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='deliveryadress',
            name='gst',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='deliveryadress',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='deliveryadress',
            name='phone_no',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='deliveryadress',
            name='vendor_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
