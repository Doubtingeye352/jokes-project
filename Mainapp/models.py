from django.db import models

# Create your models here.

class pic(models.Model):
    name = models.CharField(max_length=1000)
    picture = models.ImageField(upload_to="images/")
    date= models.CharField(max_length=200)
    