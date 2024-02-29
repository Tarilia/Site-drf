from rest_framework import generics

from site_drf.drf.models import Sitedrf
from site_drf.drf.serializers import DogSerializer


class DogAPIList(generics.ListCreateAPIView):
    queryset = Sitedrf.objects.all()
    serializer_class = DogSerializer

# class DogAPIView(generics.ListAPIView):
#     queryset = Sitedrf.objects.all()
#     serializer_class = DogSerializer
