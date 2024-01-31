# Generated by Django 5.0 on 2024-01-22 12:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareholderfund', '0002_shareholderfuns'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='shareholderfuns',
            name='amount_Debit',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shareholderfuns',
            name='amount_credit',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='RdPerson',
            fields=[
                ('rdp_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RDCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_collected', models.DecimalField(decimal_places=2, max_digits=10)),
                ('remarks', models.TextField(blank=True)),
                ('collection_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shareholderfund.rdperson')),
            ],
        ),
    ]