from django.db import models

class Visitors(models.Model):
    ip_address = models.GenericIPAddressField(primary_key=True)
    phone = models.CharField(max_length=11)
    agreement = models.BooleanField(default=False)
    comment = models.TextField(max_length=255, blank=True)
    
    def __str__(self):
        return self.phone