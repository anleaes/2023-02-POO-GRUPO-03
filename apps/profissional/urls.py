from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'Profissional'

router = routers.DefaultRouter()
router.register('', views.ProfissionalViewSet, basename='Profissional')

urlpatterns = [
    path('', include(router.urls) )
]