from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import model_to_dict
from django.utils.timezone import now

from cmdb.models import BoardInfo

import datetime


def add_system_log(sender, instance, created, **kwargs):
    now = datetime.datetime.now()
    msg = "创建对象" if created else "更新对象"

    # 获取当前对象字段
    current_fields = model_to_dict(instance)

    # 如果是更新,获得上一版本字段
    if not created:
        prev_fields = model_to_dict(instance.history.first())

    # 拼接变更详情
    details = ""
    if not created:
        changed_fields = get_changed_fields(prev_fields, current_fields)
        if changed_fields:
            details = f",变更字段:{changed_fields}"

    # 拼接记录
    record = f"{now.strftime('%Y-%m-%d %H:%M:%S')} - {msg}{details}"

    # 保存记录
    instance.maintain_records += f"\n{record}"
    instance.save()


def get_changed_fields(old, new):
    changed = []
    for k, v in old.items():
        if v != new[k]:
            changed.append(k)
    return changed
