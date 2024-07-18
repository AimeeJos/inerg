from django.db import models

class FileUpload(models.Model):    
    file = models.FileField(
        null=True,
        blank=True,
        upload_to='uploads/')    

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True)
      
    
class ProductionData(models.Model):    
    well_no = models.CharField(max_length=100,blank=True,null=True)
    oil = models.IntegerField(null=True,blank=True)
    gas = models.IntegerField(null=True,blank=True)
    brine = models.IntegerField(null=True,blank=True)
    