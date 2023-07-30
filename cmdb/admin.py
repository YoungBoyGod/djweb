from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import PCInfo, OSInfo, BoardInfo, AccessoryInfo


class PCInfoAdmin(SimpleHistoryAdmin,admin.ModelAdmin):
    list_display = (
        'device_code', 'cpu_arch', 'cpu_model', 'chassis_type', 'memory_size', 'hard_disk_size')
    list_filter = (
        'cpu_arch', 'chassis_type')  # Add filters for CPU type and chassis type

    ordering = ['cpu_arch', 'chassis_type', 'device_code']  # Sort by CPU type, chassis type, and device code


admin.site.register(PCInfo, PCInfoAdmin)


# 注册 PCInfo 模型
# admin.site.register(PCInfo)


class OSInfoAdmin(SimpleHistoryAdmin,admin.ModelAdmin):
    list_display = ('ip', 'device_type', 'os_login_user', 'os_login_password', 'bmc_ip')
    list_filter = ('device_type',)

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if obj and obj.device_type in ['PC', '工控机', '虚拟机']:
            fields.remove('bios_password')
            fields.remove('bmc_ip')
            fields.remove('bmc_user')
            fields.remove('bmc_password')
        return fields

    # Custom action functions...

    # Register custom actions...

    ordering = ['ip']


admin.site.register(OSInfo, OSInfoAdmin)


# 注册 OSInfo 模型
# admin.site.register(OSInfo)


class BoardInfoAdmin(SimpleHistoryAdmin,admin.ModelAdmin):
    list_display = ('model', 'serial_number', 'get_cooling_method_display')
    list_filter = ('cooling_method', 'model')

    ordering = ['serial_number']


# 注册 BoardInfo 模型
admin.site.register(BoardInfo, BoardInfoAdmin)

# 注册 AccessoryInfo 模型

admin.site.register(AccessoryInfo)
