from django.db import models




# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    def __str__(self):
        return f"{self.name} - {self.email}- {self.position} - {self.mobile}"