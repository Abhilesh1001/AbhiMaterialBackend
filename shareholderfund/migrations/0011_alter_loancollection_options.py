# Generated by Django 5.0 on 2024-01-25 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shareholderfund', '0010_loanamount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='loancollection',
            options={'permissions': [('view_profileupdate', 'Can view profile updates'), ('change_profileupdate', 'Can change profile updates'), ('add_profileupdate', 'Can add profile updates'), ('delete_profileupdate', 'Can delete profile updates')]},
        ),
    ]
