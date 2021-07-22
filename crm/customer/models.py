from django.db import models


class customers(models.Model):
    name = models.CharField(max_length=30, default='', blank=True, null=True)
    email = models.EmailField(max_length=50, unique=True ,default='')
    course = models.CharField(max_length=50, default='', blank=True, null=True)
    interest = models.CharField(max_length=100, default='', blank=True, null=True)


    def __str__(self):
        return  self.name