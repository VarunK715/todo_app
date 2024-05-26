from django.db import models
from django.contrib.auth.models import User

class ToDoApp(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.TextField()
    is_task_completed = models.BooleanField(default=False)
    completed_task_at = models.DateTimeField(null=True,blank=True)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='Medium')
    due_date = models.DateField(null=True, blank=True)

    #below function return name of task as title in admin page
    def __str__(self):
        return self.task