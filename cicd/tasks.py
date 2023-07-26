from celery import shared_task
# from .models import JenkinsBuild
# from .api import get_jenkins_build_data  # Import the Jenkins API function


from .models import JenkinsBuild
import jenkins
from datetime import datetime


@shared_task
def get_jenkins_build_data():
    server = jenkins.Jenkins('http://10.2.24.135:8080', username='luo', password='luo')
    jobs = server.get_all_jobs()
    build_data = []
    for job in jobs:
        builds = server.get_job_info(job['name'])['builds']

        for build in builds:
            # print(build)
            build_info = server.get_build_info(job['name'], build['number'])
            build_date = datetime.fromtimestamp(build_info['timestamp'] / 1000)
            build_data.append({
                'task_name': job['name'],
                'build_url': build['url'],
                'build_date': str(build_date),
                'build_file_name': 'example_build_file_name',
                'build_file_url': 'example_build_file_url',
                'local_download_path': 'example_local_download_path',
            })
    # print(build_data)
    return build_data


# @shared_task
def process_jenkins_build_data(build_data):
    for data in build_data:
        JenkinsBuild.objects.create(
            task_name=data['task_name'],
            build_url=data['build_url'],
            build_date=str(data['build_date']),
            build_file_name=data['build_file_name'],
            build_file_url=data['build_file_url'],
            local_download_path=data['local_download_path'],
        )


@shared_task
def monitor_jenkins_builds():
    # Call the get_jenkins_build_data() task to fetch Jenkins build data
    build_data = get_jenkins_build_data()
    print(build_data)

    # Call the process_jenkins_build_data() task to process and save the data to the database
    process_jenkins_build_data.delay(build_data)
