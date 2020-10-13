from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=50)
    fullName = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    age = models.IntegerField()

    def __str__(self):
        return self.username