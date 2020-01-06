from django.db import models
from django.db.models.signals import post_save, pre_save, pre_delete

# Create your models here.
class City(models.Model):
    name=models.CharField(max_length=30)


    def __str__(self):
        return self.name

    