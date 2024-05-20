from django.db import models
from django.contrib.auth.models import User

class ToDoApp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.TextField()
    is_task_completed = models.BooleanField(default=False)
    completed_task_at = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.task