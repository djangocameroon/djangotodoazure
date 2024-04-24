from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=30)
    completed  = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title