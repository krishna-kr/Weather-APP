from django.db import models

class Employee(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    emp_id = models.IntegerField()

    def __str__(self):
        return self.firstName

