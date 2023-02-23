from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Broker(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
  name = models.CharField(max_length=200)
  lastname = models.CharField(max_length=200)
  email = models.EmailField(max_length = 254)
  phone = models.CharField(max_length=15)
  description = models.TextField(blank=True)
  photo = models.ImageField(upload_to='broker',null=True, blank=True)
  active = models.BooleanField()

class Company(models.Model):
  id_admin = models.IntegerField(blank=True,null=True)
  comp_Name = models.CharField(max_length=200)
  comp_Logo = models.ImageField(upload_to='logo', null=True, blank=True)
  comp_Number = models.CharField(max_length=15)
  comp_mail =models.EmailField(max_length = 254)
  comp_domain = models.TextField(blank=True)
  comp_adress = models.TextField(blank=True)
  comp_city = models.TextField(blank=True)
  description = models.TextField(blank=True)
  active = models.BooleanField()
  brokers = models.ManyToManyField(Broker,blank=True)


class date_helper(models.Model):
  date_time = models.TextField()

class Properties(models.Model):
  id_broker = models.ForeignKey(Broker,on_delete=models.CASCADE,blank=True,null=True)
  title = models.TextField(blank=True)
  types  = models.CharField(max_length=100)
  city =  models.TextField(blank=True)
  adress = models.TextField(blank=True)
  living_area = models.TextField(blank=True)
  land_size = models.CharField(max_length=50)
  rooms = models.TextField(blank=True)
  price = models.IntegerField(blank=True,null=True)
  properties = models.ImageField(upload_to='properties',null=True, blank=True)
  description = models.TextField(blank=True)
  date_time = models.ManyToManyField(date_helper, blank=True)

class Sold(models.Model):
  city = models.TextField(blank=True)
  types  = models.CharField(max_length=100)
  living_area = models.TextField(blank=True)
  land_size = models.CharField(max_length=50)
  date =  models.DateField(auto_now_add=True)

class Seller(models.Model):
  city = models.TextField(blank=True)
  types  = models.CharField(max_length=100)
  living_area = models.TextField(blank=True)
  phone = models.CharField(max_length=15)
  email = models.CharField(max_length=256)
  name = models.CharField(max_length=100)
  socail_number = models.TextField(blank=True)