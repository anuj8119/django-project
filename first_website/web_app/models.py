from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    addrss = models.CharField(max_length=50, null=True, blank=True)
    age = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
    