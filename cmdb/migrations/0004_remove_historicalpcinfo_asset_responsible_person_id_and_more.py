# Generated by Django 4.2.3 on 2023-07-31 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0003_remove_historicalpcinfo_asset_responsible_person_username_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalpcinfo',
            name='asset_responsible_person_id',
        ),
        migrations.RemoveField(
            model_name='pcinfo',
            name='asset_responsible_person_id',
        ),
    ]
