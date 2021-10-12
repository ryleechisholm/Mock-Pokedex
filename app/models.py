from django.db import models

class Settings(models.Model):
    type = models.BooleanField()
