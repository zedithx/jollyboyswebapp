from django.db import models
import os
# Create your models here

def path_and_rename(name, filename):
    upload_to = 'images/'
    ext = filename.split('.')[-1]
    # get filename
    filename = '{}.{}'.format(name, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

class Tee(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(default=0, null=True, blank=True)
    size = models.CharField(max_length=200, null=True)
    length = models.CharField(max_length=200, null=True)
    ptp = models.CharField(max_length=200, null=True)
    sold = models.BooleanField(default=False, null=True)
    image = models.ImageField(upload_to=path_and_rename, height_field=None, width_field=None, max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Pant(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(default=0, null=True, blank=True)
    waist = models.CharField(max_length=200, null=True)
    inseam = models.CharField(max_length=200, null=True)
    rise = models.CharField(max_length=200, null=True)
    sold = models.BooleanField(default=False, null=True)
    image = models.ImageField(upload_to=path_and_rename, height_field=None, width_field=None, max_length=100, null=True,
                              blank=True)

    def __str__(self):
        return self.name

class Hoodies_Sweater(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(default=0, null=True, blank=True)
    size = models.CharField(max_length=200, null=True)
    length = models.CharField(max_length=200, null=True)
    ptp = models.CharField(max_length=200, null=True)
    sold = models.BooleanField(default=False, null=True)
    image = models.ImageField(upload_to=path_and_rename, height_field=None, width_field=None, max_length=100, null=True,
                              blank=True)

    def __str__(self):
        return self.name

class Exclusive_Apparel(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(default=0, null=True, blank=True)
    size = models.CharField(max_length=200, null=True)
    length = models.CharField(max_length=200, null=True)
    ptp = models.CharField(max_length=200, null=True)
    sold = models.BooleanField(default=False, null=True)
    image = models.ImageField(upload_to=path_and_rename, height_field=None, width_field=None, max_length=100, null=True,
                              blank=True)

    def __str__(self):
        return self.name
