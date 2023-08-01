# cmdb/models.py


from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from simple_history.models import HistoricalRecords
from django.core.validators import validate_ipv46_address
from django import forms
from django.contrib.auth.models import User
import json
from django.db.models.signals import post_save
from django.dispatch import receiver


class PersonnelInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="姓名")
    # department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="部门")
    email = models.EmailField(max_length=100, verbose_name="电子邮件")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "人员信息"
        verbose_name_plural = "人员信息"


class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name="部门名称")
    leader = models.CharField(max_length=100, verbose_name="部门领导")
    staff = models.ManyToManyField(PersonnelInfo)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "部门信息"
        verbose_name_plural = "部门信息"


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

    class Meta:
        verbose_name = "系统信息"
        verbose_name_plural = "系统信息"


class BoardInfo(models.Model):
    model = models.CharField(max_length=100, verbose_name="板卡型号")
    serial_number = models.CharField(max_length=100, unique=True, verbose_name="板卡编号")
    COOLING_CHOICES = (
        ('active', '主动'),
        ('passive', '被动'),
    )
    cooling_method = models.CharField(max_length=20, choices=COOLING_CHOICES, verbose_name="散热方式", default="passive")
    received_time = models.DateField(blank=True, null=True)
    received_person = models.CharField(max_length=32, blank=True, null=True, verbose_name="领取人")
    installed_time = models.DateField(blank=True, null=True)
    maintain_records = models.TextField(blank=True, null=True, verbose_name="维护记录")

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.model} - {self.serial_number} - {self.get_cooling_method_display()}"

    class Meta:
        verbose_name = "板卡信息"
        verbose_name_plural = "板卡信息"


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

    location = models.CharField(max_length=100, verbose_name="所在位置", default="办公室")
    asset_responsible_person_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="资产责任人")

    history = HistoricalRecords()

    def __str__(self):
        return self.device_code

    class Meta:
        verbose_name = "机器信息"
        verbose_name_plural = "机器信息"


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

    class Meta:
        verbose_name = "配件信息"
        verbose_name_plural = "配件信息"


class SummaryInfo(models.Model):
    # ForeignKey to PCInfo
    pc_info = models.OneToOneField(PCInfo, on_delete=models.CASCADE, verbose_name="PC信息", related_name="summary_info")

    # ForeignKey to BoardInfo (Many boards can be associated with a PC)
    boards = models.ManyToManyField(BoardInfo, verbose_name="板卡信息", related_name="summary_info")

    # ForeignKey to OSInfo
    os_info = models.OneToOneField(OSInfo, on_delete=models.CASCADE, verbose_name="OS信息", related_name="summary_info")

    # ForeignKey to AccessoryInfo
    accessory_info = models.OneToOneField(AccessoryInfo, on_delete=models.CASCADE, verbose_name="配件信息",
                                          related_name="summary_info")

    # Additional fields for the SummaryInfo model, if any
    # ...

    history = HistoricalRecords()

    def __str__(self):
        return f"Summary Info: {self.pc_info.device_code}"

    class Meta:
        verbose_name = "汇总信息"
        verbose_name_plural = "汇总信息"


