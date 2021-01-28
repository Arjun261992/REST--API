from django.db import models

# Create your models here.
class employees(models.Model):
    first_name= models.CharField(max_length=15)
    last_name= models.CharField(max_length=15)
    email= models.CharField(max_length=20)
    phone= models.IntegerField()

    def __str__(self):
       return self.first_name

