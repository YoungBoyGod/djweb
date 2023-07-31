# Generated by Django 4.2.3 on 2023-07-31 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0005_alter_accessoryinfo_options_alter_boardinfo_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardinfo',
            name='installed_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='boardinfo',
            name='maintain_records',
            field=models.TextField(blank=True, null=True, verbose_name='维护记录'),
        ),
        migrations.AddField(
            model_name='boardinfo',
            name='received_person',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='领取人'),
        ),
        migrations.AddField(
            model_name='historicalboardinfo',
            name='installed_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historicalboardinfo',
            name='maintain_records',
            field=models.TextField(blank=True, null=True, verbose_name='维护记录'),
        ),
        migrations.AddField(
            model_name='historicalboardinfo',
            name='received_person',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='领取人'),
        ),
    ]