from django.urls import path
from .views import get_jenkins_build_data_view

urlpatterns = [
    path('get_jenkins_build_data/', get_jenkins_build_data_view, name='get_jenkins_build_data'),
]