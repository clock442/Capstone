from django.db import models
import string

class Gym(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    map_image = models.ImageField(upload_to='images/', default='../uploaded_files/images/kitten1200x800.jpg')

    def __str__(self):
        return self.name

class WallType(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class HoldType(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Route(models.Model):
    name = models.CharField(max_length=100)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE, related_name='routes')
    wall_type = models.ForeignKey(WallType, on_delete=models.CASCADE, related_name='wall_type')
    hold_types = models.ManyToManyField(HoldType, related_name='hold_types')
    rating = models.IntegerField()
    height = models.IntegerField()
    description = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    date_leaving = models.DateTimeField(null=True, blank=True)
    x_position = models.IntegerField()
    y_position = models.IntegerField()
    def __str__(self):
        return self.name + ' ' + self.rating 

