from django.db import models

class Settings(models.Model):
    type = models.BooleanField()


class Created_mon(models.Model):
    Creator = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.IntegerField()
    region = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    type1 = models.CharField(max_length=100)
    type2 = models.CharField(max_length=100)

def create_mon(Creator, name, height, weight, region, description, type1, type2):
    new_mon = Created_mon(Creator=Creator, name=name, height=height, weight=weight, region=region, description=description, type1=type1, type2=type2)
    new_mon.save()
    return new_mon
