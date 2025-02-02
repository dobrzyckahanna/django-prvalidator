from django.contrib import admin
from .models import Project, Story, Task

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'name', 'description', 'status')
    list_editable = ('owner', 'status')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'creator', 'assigned_to', 'name', 'status')
    list_editable = ('assigned_to', 'status')

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'creator', 'assigned_to', 'name', 'status')
    list_editable = ('assigned_to', 'status')