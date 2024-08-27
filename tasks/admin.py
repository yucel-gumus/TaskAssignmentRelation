from django.contrib import admin

from django.contrib import admin
from .models import Person, Task, PersonTaskAssignment

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(PersonTaskAssignment)
class PersonTaskAssignmentAdmin(admin.ModelAdmin):
    list_display = ('person', 'task', 'frequency', 'last_completion_time')
