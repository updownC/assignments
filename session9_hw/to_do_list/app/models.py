from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    due = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))

    def __str__(self):
        return self.title