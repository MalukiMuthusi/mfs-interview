from pyexpat import model
from django.db import models


# A cartesian point
class Point(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()

    def __str__(self) -> str:
        return super().__str__()

# Holds all the points that have been submitted to calculated which points are nearest to each other
class Nearest(models.Model):
    
    point_to = models.ManyToManyField(Point) # point 1 of the points nearest to each other
    distance = models.FloatField() # shortest distance between 2 points