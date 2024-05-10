from django.db import models

class ToDoApp(models.Model):
    task = models.TextField()
    is_task_completed = models.BooleanField(default=False)
    completed_task_at = models.DateTimeField(null=True,blank=True)