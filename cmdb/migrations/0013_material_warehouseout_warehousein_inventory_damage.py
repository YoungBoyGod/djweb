# Generated by Django 4.2.3 on 2023-08-01 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cmdb', '0012_alter_boardinfo_maintain_records_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('stock', models.IntegerField(default=0)),
                ('location', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='materials')),
                ('remarks', models.TextField(blank=True, max_length=500)),
                ('serial_numbers', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WarehouseOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('date', models.DateField()),
                ('serial_number', models.CharField(max_length=50)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.material')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WarehouseIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('date', models.DateField()),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.material')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('date', models.DateField()),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.material')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Damage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('date', models.DateField()),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.material')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
