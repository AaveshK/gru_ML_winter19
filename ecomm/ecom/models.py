from django.db import models
from django.urls import path
#DataFlair Models
class Product(models.Model):
    #Table 1
    name = models.CharField(max_length = 64)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name

class Clothing(models.Model):
    #Table 1
    name = models.CharField(max_length = 64)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name

class Electronics(models.Model):
    #Table 1
    name = models.CharField(max_length = 64)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name

class Books(models.Model):
    #Table 1
    name = models.CharField(max_length = 64)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name

class Kitchen(models.Model):
    #Table 1
    name = models.CharField(max_length = 64)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name

class Sports(models.Model):
    #Table 1
    name = models.CharField(max_length = 64)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name


