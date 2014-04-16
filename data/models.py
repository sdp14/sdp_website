from django.db import models
from json_field import JSONField
# Create your models here.

class Data(models.Model):
   title = models.CharField(max_length=200)
   def __unicode__(self):
       return self.title
	   
class JSONModel(models.Model):

   json_model = JSONField()
   def __unicode__(self):
       return self.title

class JSONModel_Tram(models.Model):

   tram_info = JSONField()
   def __unicode__(self):
       return self.title	   