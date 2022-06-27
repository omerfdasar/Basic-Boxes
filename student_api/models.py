from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)
    # blank=True for admin dashboard
    # null=True for db

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
