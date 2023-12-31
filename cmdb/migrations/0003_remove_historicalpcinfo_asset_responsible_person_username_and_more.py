# Generated by Django 4.2.3 on 2023-07-31 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0002_remove_historicalpcinfo_asset_responsible_person_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalpcinfo',
            name='asset_responsible_person_username',
        ),
        migrations.RemoveField(
            model_name='pcinfo',
            name='asset_responsible_person_username',
        ),
        migrations.AddField(
            model_name='historicalpcinfo',
            name='asset_responsible_person_id',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='historicalpcinfo',
            name='asset_responsible_person_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='资产负责人'),
        ),
        migrations.AddField(
            model_name='pcinfo',
            name='asset_responsible_person_id',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='pcinfo',
            name='asset_responsible_person_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='资产负责人'),
        ),
    ]
