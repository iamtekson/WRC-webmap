from django.db import models
from django.contrib.gis.db import models as gis_models
from datetime import datetime

class points(models.Model):
    title = models.CharField(max_length=30)
    location = gis_models.PointField(srid = 4326)
    objects = models.Manager()

    def __str__(self):
        return self.title

class roadNetwork(models.Model):
    road_name = models.CharField(max_length=50)
    width = models.CharField(max_length=50)
    buffer_are = models.FloatField()
    type = models.CharField(max_length=50)
    geom = gis_models.MultiLineStringField(srid=4326)

    def __str__(self):
        return self.road_name

class waterPipeLine(models.Model):
    diameter = models.IntegerField()
    meterial = models.CharField(max_length=50)
    where_from = models.CharField(max_length=50)
    towhere = models.CharField(max_length=50)
    geom = gis_models.MultiLineStringField(srid=4326)

    def __str__(self):
        return self.where_from

class wifiCable(models.Model):
    core = models.IntegerField()
    mbps = models.IntegerField()
    from_field = models.CharField(max_length=50)
    to = models.CharField(max_length=50)
    geom = gis_models.MultiLineStringField(srid=4326)

    def __str__(self):
    	return self.from_field

class wifiNode(models.Model):
    router_poi = models.CharField(max_length=50)
    geom = gis_models.MultiPointField(srid=4326)

    def __str__(self):
        return self.router_poi