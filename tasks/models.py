from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    important = models.BooleanField(default=False)

    datecompleted = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True)



    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title 

class Note(models.Model):
    description = models.TextField(null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
