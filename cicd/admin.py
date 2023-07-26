from django.contrib import admin

# Register your models here.
from .models import JenkinsBuild

admin.site.register(JenkinsBuild)