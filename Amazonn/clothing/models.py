from django.db import models

# Create your models here.
#table ka struture 

class Product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField ()
    
def __str__(self):
    return self.name
