from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from site_drf.drf.models import Sitedrf, Category
from site_drf.drf.serializers import DogSerializer


class DogViewSet(viewsets.ModelViewSet):
#     queryset = Sitedrf.objects.all()
    serializer_class = DogSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Sitedrf.objects.all()[:3]

        return Sitedrf.objects.filter(pk=pk)

    @action(methods=['get'], detail=False)
    def category(self, request):
        cat = Category.objects.all()
        return Response({'cat': [c.name for c in cat]})


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
