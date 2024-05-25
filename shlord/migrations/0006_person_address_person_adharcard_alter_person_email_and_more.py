# Generated by Django 4.2.5 on 2024-04-15 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shlord', '0005_asset_asset_name_fixeddeposite_person_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='person',
            name='adharcard',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='pan_no',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone_no',
            field=models.CharField(default='', max_length=15),
        ),
    ]