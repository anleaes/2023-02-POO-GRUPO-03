from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'Cliente'

router = routers.DefaultRouter()
router.register('', views.RegistroVacinaçãoViewSet, basename='cliente')

urlpatterns = [
    path('', include(router.urls) )
]