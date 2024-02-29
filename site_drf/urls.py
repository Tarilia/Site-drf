from django.contrib import admin
from django.urls import path

from site_drf.drf.views import DogAPIList, DogAPIUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/doglist/', DogAPIList.as_view()),
    path('api/doglist/<int:pk>/', DogAPIUpdate.as_view()),
#     path('api/doglist/', DogAPIView.as_view()),
]
