from django.db import models
# from django.utils import timezone
# from datetime import timedelta


class Visitors(models.Model):
    ip_address = models.GenericIPAddressField(primary_key=True)
    phone = models.CharField(max_length=11, unique=True)
    agreement = models.BooleanField(default=False)
    comment = models.TextField(max_length=255, blank=True)
    
    def __str__(self):
        return self.phone

class Counter(models.Model):
    count = models.PositiveIntegerField(default=0)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return f'{self.date} : {self.count}'