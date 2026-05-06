from django.db import models
from django.contrib.auth import AbstractUser

class User(AbstractUser):
    def __str__(self):
        return self.username
