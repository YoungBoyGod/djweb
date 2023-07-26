# cicd/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import JenkinsBuild
# from .api import get_jenkins_build_data
from .tasks import process_jenkins_build_data, get_jenkins_build_data  # Import the Celery task


@api_view(['GET'])
def get_jenkins_build_data_view(request):
    build_data = get_jenkins_build_data()
    # print(build_data)
    process_jenkins_build_data(build_data)  # Invoke Celery task asynchronously
    return Response({'message': 'Jenkins build data processing started.'})
