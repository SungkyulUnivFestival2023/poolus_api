from .models import Visitors
from rest_framework import serializers

class VisitorsSerializer(serializers.ModelSerializer):
    ip_address = serializers.ReadOnlyField() 
    
    class Meta:
        model = Visitors
        fields = ['ip_address', 'phone', 'agreement', 'comment']