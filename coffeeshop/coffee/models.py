from django.db import models

class Coffee(models.Model):
    name = models.CharField('Name', max_length=20)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField('Image',max_length=2083)
    
