from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=100)
    keyword = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}"

        