# cmdb/models.py

from django.db import models
from simple_history.models import HistoricalRecords
from django.core.validators import validate_ipv46_address


class OSInfo(models.Model):
    DEVICE_TYPES = (
        ('服务器', '服务器'),
        ('PC', 'PC'),
        ('工控机', '工控机'),
        ('虚拟机', '虚拟机'),
    )

    ip = models.GenericIPAddressField(unique=True, verbose_name="IP 地址", validators=[validate_ipv46_address])
    device_type = models.CharField(max_length=100, choices=DEVICE_TYPES, verbose_name="设备类型")
    bios_password = models.CharField(max_length=100, blank=True, null=True, verbose_name="BIOS 密码")
    os_login_user = models.CharField(max_length=100, verbose_name="OS 登录用户")
    os_login_password = models.CharField(max_length=100, verbose_name="OS 登录密码")
    bmc_ip = models.GenericIPAddressField(blank=True, null=True, verbose_name="BMC IP")
    bmc_user = models.CharField(max_length=100, blank=True, null=True, verbose_name="BMC 用户")
    bmc_password = models.CharField(max_length=100, blank=True, null=True, verbose_name="BMC 密码")

    history = HistoricalRecords()

    def __str__(self):
        return self.ip


class BoardInfo(models.Model):
    model = models.CharField(max_length=100, verbose_name="板卡型号")
    serial_number = models.CharField(max_length=100, unique=True, verbose_name="板卡编号")
    COOLING_CHOICES = (
        ('active', '主动'),
        ('passive', '被动'),
    )
    cooling_method = models.CharField(max_length=20, choices=COOLING_CHOICES, verbose_name="散热方式", default="passive")
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.model} - {self.serial_number} - {self.get_cooling_method_display()}"


# user = models.CharField(max_length=100, verbose_name="使用人")
#     project = models.CharField(max_length=100, verbose_name="使用项目")
#     location = models.CharField(max_length=100, verbose_name="所在区域")
#     rack_number = models.CharField(max_length=100, verbose_name="具体机架")
class PCInfo(models.Model):
    device_code = models.CharField(max_length=100, unique=True, verbose_name="设备编码", default='00000')
    cpu_arch = models.CharField(max_length=100, verbose_name="CPU 架构")
    cpu_model = models.CharField(max_length=100, verbose_name="CPU 型号")
    chassis_type = models.CharField(max_length=100, verbose_name="机箱类型")
    memory_size = models.CharField(max_length=100, verbose_name="内存大小")  # Add memory size field
    hard_disk_size = models.CharField(max_length=100, verbose_name="硬盘大小")  # Add hard disk size field

    history = HistoricalRecords()

    def __str__(self):
        return self.device_code


class AccessoryInfo(models.Model):
    device_model = models.CharField(max_length=100, verbose_name="设备型号")
    device_name = models.CharField(max_length=100, verbose_name="设备名称")
    device_description = models.TextField(verbose_name="设备描述")
    entry_date = models.DateTimeField(verbose_name="入库时间", auto_now_add=True)
    recipient = models.CharField(max_length=100, verbose_name="领取人")
    borrow_date = models.DateField(null=True, blank=True, verbose_name="借用时间")
    return_date = models.DateField(null=True, blank=True, verbose_name="归还时间")

    history = HistoricalRecords()

    def __str__(self):
        return self.device_name
