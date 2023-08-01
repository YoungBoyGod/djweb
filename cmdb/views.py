from django.db.models import Q
from django.shortcuts import render

from cmdb.models import PersonnelInfo, BoardInfo


def search_view(request):
    name = request.GET.get('name')
    serial_number = request.GET.get('serial_number')

    personnel = PersonnelInfo.objects.filter(name__icontains=name)
    boards = BoardInfo.objects.filter(serial_number__icontains=serial_number)

    # 合并两个查询集
    query = personnel | boards

    results = query.distinct()

    return render(request, 'search_results.html', {'results': results})