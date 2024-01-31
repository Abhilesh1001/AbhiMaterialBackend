# Generated by Django 5.0 on 2024-01-22 17:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareholderfund', '0005_alter_rdcollection_collection_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='rdperson',
            name='email',
            field=models.EmailField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='rdperson',
            name='pan_no',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='rdperson',
            name='phone_no',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='rdperson',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]