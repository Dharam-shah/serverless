from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'created_at', 'deadline']