from django.db import models

class FlightModel(models.Model):
    fly_city = models.CharField(max_length=50)
    price_ticket = models.FloatField()
    date = models.DateField()
    description = models.TextField()

# Create your models here.
