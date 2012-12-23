from django.db import models

class Sponsor(models.Model):
    url = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='sponsorer')
    navn = models.CharField(max_length=200, blank=True)
    
    def __unicode__(self):
        return self.navn

