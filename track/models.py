from django.db import models
from datetime import datetime

class Kid(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    
    weight = models.FloatField(null=True, blank=True, default = None)
    height = models.FloatField(null=True, blank=True, default = None)
    
    born = models.DateTimeField()
    
    male = models.BooleanField()
    
    def __unicode__(self):
        return self.first_name + ' ' + self.last_name
    
    def gender(self):
        if self.male:
            return 'M'
        else:
            return 'F'
            
    
class Measurement(models.Model):
    weight = models.FloatField()
    height = models.FloatField()
    
    taken = models.DateTimeField(default=datetime.now, blank=True)
    
    child = models.ForeignKey(Kid)
    
    def __unicode__(self):
        return '{0} kg, {1} cm'.format(self.weight, self.height)