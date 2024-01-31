# Generated by Django 5.0 on 2024-01-25 13:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareholderfund', '0012_alter_loancollection_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanamount',
            name='closing_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='loanamount',
            name='opening_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]