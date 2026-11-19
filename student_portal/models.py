from django.db import models

# Create your models here.

class Student_table(models.Model):
    reg_no = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    marks = models.FloatField()
    email = models.EmailField()
    dob = models.DateField()
    def __str__(self):
        return super().__str__()