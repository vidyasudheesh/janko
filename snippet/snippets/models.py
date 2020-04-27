from django.db import models
class Snippet(models.Model):
    Name = models.CharField(max_length =255)
    Algorithem = models.CharField(max_length =255)
    Style = models.CharField(max_length=255)
    Language = models.CharField(max_length=255)
    Length = models.IntegerField()
    Paper  = models.CharField(max_length=1024)

# Create your models here.
