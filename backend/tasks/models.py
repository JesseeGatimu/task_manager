from django.db import models
from accounts.models import User
class Task(models.Model):
    STATUS_CHOICES=(
        ('completed','Completed'),
        ('pending','Pending'),
        ('inprogress','Inprogress')
    )
    title=models.CharField(max_length=50)
    description=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=100,choices=STATUS_CHOICES)
    completion_date=models.DateTimeField()

    def __str__(self):
        return f"{self.title} - {self.description}"

