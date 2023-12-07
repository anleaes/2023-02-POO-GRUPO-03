from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'tipo'

router = routers.DefaultRouter()
router.register('', views.TipoViewSet, basename='tipos')

urlpatterns = [
    path('', include(router.urls) )
]