from django.contrib import admin
from django import forms
from django.utils.timezone import now
from simple_history.admin import SimpleHistoryAdmin
from .models import PCInfo, OSInfo, BoardInfo, AccessoryInfo, SummaryInfo, PersonnelInfo, Department
from django.db.models.signals import post_save
from django.dispatch import receiver


# from django import forms


class BaseAdmin(SimpleHistoryAdmin):

    def get_search_fields(self, request):
        search_fields = [f"{name}__icontains" for name in self.list_display]
        return search_fields

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)

        for name in self.list_display:
            queryset |= self.model.objects.filter(**{f"{name}__icontains": search_term})

        return queryset, use_distinct


class DepartmentAdmin(BaseAdmin):
    list_display = ('name', 'leader')


admin.site.register(Department, DepartmentAdmin)


class PersonnelInfoAdmin(SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ('name', 'email', 'department_display')

    # search_fields  = ('name', 'email', 'department_display')

    def department_display(self, obj):
        return ", ".join([dept.name for dept in obj.department_set.all()])


admin.site.register(PersonnelInfo, PersonnelInfoAdmin)


class PCInfoForm(forms.ModelForm):
    asset_responsible_person_name = forms.ChoiceField(choices=[], required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        personnel_choices = [(p.id, p.name) for p in PersonnelInfo.objects.all()]
        personnel_choices.append((-1, '无负责人'))
        # self.fields['asset_responsible_person_name'].choices = personnel_choices
        self.fields['asset_responsible_person_name'].choices = personnel_choices

    class Meta:
        model = PCInfo
        fields = '__all__'
        # Update the verbose_name for the field
        labels = {
            'asset_responsible_person_name': '责任人',
        }


class PCInfoAdmin(BaseAdmin):
    form = PCInfoForm

    fieldsets = (
        ('基本信息', {
            'fields': (
                'device_code', 'cpu_arch', 'cpu_model', 'chassis_type', 'memory_size', 'hard_disk_size', 'location',
            ),
        }),
        ('负责人', {
            'fields': ('asset_responsible_person_name',),

        })
    )

    list_display = ('device_code', 'cpu_arch', 'cpu_model', 'chassis_type', 'memory_size', 'hard_disk_size', 'location',
                    'asset_responsible_person_name')
    list_filter = ('cpu_arch', 'chassis_type', 'location')
    ordering = ['cpu_arch', 'chassis_type', 'device_code']

    def save_model(self, request, obj, form, change):
        responsible_person_id = form.cleaned_data.get('asset_responsible_person_name')
        if responsible_person_id and responsible_person_id != '-1':
            responsible_person = PersonnelInfo.objects.get(id=responsible_person_id)
            obj.asset_responsible_person_name = responsible_person.name
        else:
            obj.asset_responsible_person_name = '无负责人'

        super().save_model(request, obj, form, change)


admin.site.register(PCInfo, PCInfoAdmin)


# 注册 PCInfo 模型
# admin.site.register(PCInfo)


class OSInfoAdmin(BaseAdmin):
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


class BoardInfoAdmin(BaseAdmin):
    received_time = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    list_display = (
        'model', 'received_person', 'serial_number', 'cooling_method', 'received_time', 'maintain_records')
    list_filter = ('cooling_method', 'model')

    ordering = ['serial_number']

    # 注册 BoardInfo 模型


admin.site.register(BoardInfo, BoardInfoAdmin)

# 注册 AccessoryInfo 模型

admin.site.register(AccessoryInfo)


class SummaryInfoAdmin(SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = (
        'os_info', 'board_model', 'board_cooling_method', 'pc_cpu_arch', 'pc_cpu_model', 'pc_chassis_type',
        'accessory_info', 'pc_device_code', 'get_responsible_person')
    list_select_related = ('pc_info', 'os_info', 'accessory_info')

    def get_responsible_person(self, obj):
        return obj.pc_info.asset_responsible_person_name

    get_responsible_person.short_description = '责任人'

    def pc_device_code(self, obj):
        return obj.pc_info.device_code

    pc_device_code.short_description = '设备编码'

    def pc_cpu_arch(self, obj):
        return obj.pc_info.cpu_arch

    pc_cpu_arch.short_description = 'CPU 架构'

    def pc_cpu_model(self, obj):
        return obj.pc_info.cpu_model

    pc_cpu_model.short_description = 'CPU 型号'

    def pc_chassis_type(self, obj):
        return obj.pc_info.chassis_type

    pc_chassis_type.short_description = '机箱类型'

    def board_model(self, obj):
        return ', '.join(board.model for board in obj.boards.all())

    board_model.short_description = '板卡型号'

    def board_cooling_method(self, obj):
        return ', '.join(board.get_cooling_method_display() for board in obj.boards.all())

    board_cooling_method.short_description = '散热方式'


admin.site.register(SummaryInfo, SummaryInfoAdmin)
