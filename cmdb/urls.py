from django.urls import path
from . import views
# # from .views import get_jenkins_build_data_view
# #
urlpatterns = [
    path('search/<str:name>/<str:serial_number>/', views.search_view, name='search'),
]


