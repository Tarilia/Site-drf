from django.contrib import admin
from django.urls import path

from site_drf.drf.views import (DogAPIList, DogAPIUpdate,
                                DogAPIDetail, DogViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/doglist/', DogViewSet.as_view({'get': 'list'})),
    path('api/doglist/<int:pk>/', DogViewSet.as_view({'put': 'update'})),
#     path('api/dogdetail/<int:pk>/', DogAPIDetail.as_view()),
#     path('api/doglist/', DogAPIView.as_view()),
]
