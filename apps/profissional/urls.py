from django.urls import path, include
from . import views
from rest_framework import routers

#app_name = 'Profissional'
app_name = 'profissional'

router = routers.DefaultRouter()
#router.register('', views.ProfissionalViewSet, basename='Profissional')
router.register('', views.ProfissionalViewSet, basename='profissionais')

urlpatterns = [
    path('', include(router.urls) )
]