from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    get_readonly_fields = ("created", "updated")

admin.site.register(Project)