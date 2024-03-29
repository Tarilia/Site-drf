from django.contrib import admin
from django.urls import path, include, re_path

from site_drf.drf.views import DogAPIList, DogAPIUpdate, DogAPIDestroy
# from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'dog', DogViewSet, basename='dog')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/dog/', DogAPIList.as_view()),
    path('api/dog/<int:pk>/', DogAPIUpdate.as_view()),
    path('api/dogdelete/<int:pk>/', DogAPIDestroy.as_view()),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
#     path('api/', include(router.urls))
#     path('api/doglist/', DogViewSet.as_view({'get': 'list'})),
#     path('api/doglist/<int:pk>/', DogViewSet.as_view({'put': 'update'})),
#     path('api/dogdetail/<int:pk>/', DogAPIDetail.as_view()),
#     path('api/doglist/', DogAPIView.as_view()),
]
