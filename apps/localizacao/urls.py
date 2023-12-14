from django.urls import path, include
from . import views
from rest_framework import routers

#app_name = 'Localizacao'
app_name = 'localizacao'

router = routers.DefaultRouter()
#router.register('', views.LocalizacaoViewSet, basename='Localizacao')
router.register('', views.LocalizacaoViewSet, basename='localizacoes')

urlpatterns = [
    path('', include(router.urls) )
]