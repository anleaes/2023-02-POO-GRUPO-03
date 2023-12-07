from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'servico'

router = routers.DefaultRouter()
router.register('', views.ServicoViewSet, basename='servicos')

urlpatterns = [
    path('', include(router.urls) )
]