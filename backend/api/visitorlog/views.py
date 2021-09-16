from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from visitorlog.serializers import LogSerializer
from visitorlog.models import Log


class LogViewSet(viewsets.ModelViewSet):
   queryset = Log.objects.all()
   serializer_class = LogSerializer