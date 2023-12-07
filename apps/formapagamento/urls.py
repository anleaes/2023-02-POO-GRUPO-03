from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'FormasDePagamento'

router = routers.DefaultRouter()
router.register('', views.RegistroVacinaçãoViewSet, basename='formapagamento')

urlpatterns = [
    path('', include(router.urls) )
]