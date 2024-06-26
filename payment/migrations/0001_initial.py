# Generated by Django 4.2.5 on 2024-03-30 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goodreceipt', '0006_materialissue_remarks_alter_mir_mir_no'),
        ('material', '0009_materialgroup_materialunit'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentTovendor',
            fields=[
                ('payment_no', models.AutoField(primary_key=True, serialize=False)),
                ('amount_debit', models.DecimalField(decimal_places=3, max_digits=10)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('miro_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goodreceipt.mir')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AdvancePayment',
            fields=[
                ('advance_payment_no', models.AutoField(primary_key=True, serialize=False)),
                ('amount_debit', models.DecimalField(decimal_places=3, max_digits=10)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('po_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.purchaseorder')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
