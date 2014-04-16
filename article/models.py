from django.db import models
from time import time


# Create your models here.
class Article(models.Model):
   title = models.CharField(max_length=200)
   def __unicode__(self):
       return self.title


def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.', '_'), filename)

def upload_file_name(instance, filename):
    return "tram_commands/%s_%s" % (str(time()).replace('.', '_'), filename)
	
	
class File_Upload(models.Model):
    uploaded_file = models.FileField(upload_to=get_upload_file_name)
    def __unicode__(self):
       return self.title
	   
	   
class Tram_File_Upload(models.Model):
    uploaded_file = models.FileField(upload_to=upload_file_name)
    def __unicode__(self):
       return self.title