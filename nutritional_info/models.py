from django.db import models

# Create your models here.
class receipes(models.Model):
    #Models with receipes
    name_receipe = models.CharField(max_length=200)
    image = models.ImageField()
    ingredients = models.TextField(max_length=2000)
    tutorial = models.TextField(max_length=2000)

    #nutritional info
    calories = models.FloatField(null=True, blank=True)
    carbo = models.FloatField(null=True, blank=True)
    fat = models.FloatField(null=True, blank=True)
    protein = models.FloatField(null=True, blank=True)
