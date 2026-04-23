from django.db import models

class Task(models.Model):
    STATUS_CHOICES=(
        ('completed','Completed'),
        ('in_progress','In_progress'),
        ('pending','Pending')
    )
    title=models.CharField(max_length=50)
    description=models.TextField()
    completion_date=models.DateTimeField()
    status=models.CharField(choices=STATUS_CHOICES,max_length=20,default='Pending')
    
    def __str__(self):
        return f"{self.title} - {self.status}"