from django.db import models


#
#
# # Create your models here.
# class Jenkins(models.Model):
#     project = models.CharField(max_length=100)
#     task_name = models.CharField(max_length=100)
#     build_url = models.URLField()
#     build_date = models.DateTimeField()
#     build_file = models.CharField(max_length=100)
#     build_file_url = models.URLField()
#     local_download_path = models.FilePathField()
#
#
# class MinIO(models.Model):
#     bucket = models.CharField(max_length=63)
#     folder = models.CharField(max_length=255)
#
#     object_name = models.CharField(max_length=1023)
#     download_url = models.URLField()
#     download_path = models.FilePathField()
#
#     server = models.CharField(max_length=255)
#     upload_path = models.FilePathField()
#
#
# class JiraIssue(models.Model):
#     closed = models.BooleanField()
#
#     issue_key = models.CharField(max_length=20)
#
#     issue_type = models.CharField(max_length=20, choices=(
#         ('known issue', 'Known Issue'),
#         ('test', 'Test'),
#         ('risk', 'Risk'),
#     ))
#
#     last_release_date = models.DateField()
#
#     component = models.CharField(max_length=255)
#     owner = models.CharField(max_length=255)
#
#     description = models.TextField()
#
#     vendor_info = models.TextField()
#
#
class JenkinsBuild(models.Model):
    task_name = models.CharField(max_length=100)
    build_url = models.URLField()
    build_date = models.CharField(max_length=100)
    build_file_name = models.CharField(max_length=100)
    build_file_url = models.URLField()
    local_download_path = models.CharField(max_length=200)
