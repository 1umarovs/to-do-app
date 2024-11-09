from django.db import models

# Create your models here.
PRIORITY = (
    ("red","Danger"),
    ("orange","Warning"),
    ("lightbule","Info"),
    ("green","Success"),
)

class Todo(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    priority = models.CharField(max_length=250,choices=PRIORITY)
    doned = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title