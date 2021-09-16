from rest_framework import serializers

from visitorlog.models import Log

class LogSerializer(serializers.ModelSerializer):
   class Meta:
       model = Log
       fields = ('in_time', 'first_name', 'last_name', 'email')