# Generated by Django 4.2.3 on 2023-08-01 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0010_alter_boardinfo_maintain_records_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardinfo',
            name='maintain_records',
            field=models.TextField(verbose_name='维护记录'),
        ),
        migrations.AlterField(
            model_name='historicalboardinfo',
            name='maintain_records',
            field=models.TextField(verbose_name='维护记录'),
        ),
    ]
