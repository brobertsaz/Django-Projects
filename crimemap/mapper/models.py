from django.db import models

class Crime(models.Model):
    type = models.CharField(max_length=20)
    date = models.DateField()
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=8, decimal_places=6)
    address = models.CharField(max_length=50)