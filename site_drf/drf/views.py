from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from site_drf.drf.models import Sitedrf
from sitedrf.drf.permissions import IsAdminORReadOnly
from site_drf.drf.serializers import DogSerializer


class DogAPIList(generics.ListCreateAPIView):
    queryset = Sitedrf.objects.all()
    serializer_class = DogSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class DogAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Sitedrf.objects.all()
    serializer_class = DogSerializer


class DogAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Sitedrf.objects.all()
    serializer_class = DogSerializer
    permission_classes = (IsAdminORReadOnly, )


# class DogViewSet(viewsets.ModelViewSet):
#     queryset = Sitedrf.objects.all()
#    serializer_class = DogSerializer

#    def get_queryset(self):
#        pk = self.kwargs.get('pk')
#        if not pk:
#            return Sitedrf.objects.all()[:3]

#        return Sitedrf.objects.filter(pk=pk)

#    @action(methods=['get'], detail=False)
#    def category(self, request):
#        cat = Category.objects.all()
#        return Response({'cat': [c.name for c in cat]})


# class DogAPIView(generics.ListAPIView):
#     queryset = Sitedrf.objects.all()
#     serializer_class = DogSerializer
