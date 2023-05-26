from django.db import models

class Visitors(models.Model):
    ip_address = models.GenericIPAddressField(primary_key=True)
    phone = models.CharField(max_length=11, unique=True)
    agreement = models.BooleanField(default=False)
    comment = models.TextField(max_length=255, blank=True)
    
    def __str__(self):
        return self.phone

class Counter(models.Model):
    count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f'total: {self.count}'