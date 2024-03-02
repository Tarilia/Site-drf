from rest_framework import generics, viewsets

from site_drf.drf.models import Sitedrf
from site_drf.drf.serializers import DogSerializer


class DogViewSet(viewsets.ModelViewSet):
    queryset = Sitedrf.objects.all()
    serializer_class = DogSerializer


# class DogAPIList(generics.ListCreateAPIView):
#    queryset = Sitedrf.objects.all()
#    serializer_class = DogSerializer


#class DogAPIUpdate(generics.UpdateAPIView):
#    queryset = Sitedrf.objects.all()
#    serializer_class = DogSerializer


#class DogAPIDetail(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Sitedrf.objects.all()
#    serializer_class = DogSerializer


# class DogAPIView(generics.ListAPIView):
#     queryset = Sitedrf.objects.all()
#     serializer_class = DogSerializer
