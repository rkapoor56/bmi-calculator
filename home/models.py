from django.db import models

class Entry(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    bmi = models.FloatField(null=True)