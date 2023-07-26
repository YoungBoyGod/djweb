from django.test import TestCase

# Create your tests here.



from cicd.models import JenkinsBuild
import datetime

# 添加一条Jenkins构建数据
build = JenkinsBuild(
    task_name='My Jenkins Task',
    build_url='http://jenkins_server/job/my_project/1/',
    build_date=datetime.datetime.now(),
    build_file_name='my_build_file.tar.gz',
    build_file_url='http://jenkins_server/job/my_project/1/artifact/my_build_file.tar.gz',
    local_download_path='/path/to/local/directory/',
)
build.save()