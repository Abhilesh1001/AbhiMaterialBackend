# Generated by Django 5.0 on 2024-01-24 15:01

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareholderfund', '0009_alter_loancollection_loan_person'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanAmount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField()),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('loan_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shareholderfund.loanperson')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]