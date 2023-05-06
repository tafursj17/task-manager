from django.contrib import admin
from . models import Task, Note

class TaskAdmin(admin.ModelAdmin):
    ordering=('-created',)
    list_display=("title","user", "important", "datecompleted")
    list_filter=("user", "important")
    readonly_fields = ('created',)


class NoteAdmin(admin.ModelAdmin):
    list_display=("description", "task")
    readonly_fields = ('created',)
    list_display_links=('task',)

# Register your models here.
admin.site.register(Task, TaskAdmin)
admin.site.register(Note, NoteAdmin)