from django.db import models

# Create your models here.

class Teilnehmer(models.Model):
    id = models.BigIntegerField(primary_key=True)
    vorname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    thema = models.CharField(max_length=100)
    session_chair = models.CharField(max_length=60)
    note = models.DecimalField(max_digits=2, decimal_places=1)
