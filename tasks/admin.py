from django.contrib import admin
from . models import Task, Note

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

# Register your models here.
admin.site.register(Task, TaskAdmin)
admin.site.register(Note, NoteAdmin)