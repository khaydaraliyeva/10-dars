from django.shortcuts import render
from rest_framework import viewsets
from .serializers import VideoSerializer
from .models import Video

# Create your views here.
class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer