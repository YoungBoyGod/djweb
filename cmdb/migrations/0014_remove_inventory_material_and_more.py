# Generated by Django 4.2.3 on 2023-08-01 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0013_material_warehouseout_warehousein_inventory_damage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='material',
        ),
        migrations.RemoveField(
            model_name='warehousein',
            name='material',
        ),
        migrations.RemoveField(
            model_name='warehousein',
            name='operator',
        ),
        migrations.RemoveField(
            model_name='warehouseout',
            name='material',
        ),
        migrations.RemoveField(
            model_name='warehouseout',
            name='operator',
        ),
        migrations.DeleteModel(
            name='Damage',
        ),
        migrations.DeleteModel(
            name='Inventory',
        ),
        migrations.DeleteModel(
            name='Material',
        ),
        migrations.DeleteModel(
            name='WarehouseIn',
        ),
        migrations.DeleteModel(
            name='WarehouseOut',
        ),
    ]
