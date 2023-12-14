from django.urls import path, include
from . import views
from rest_framework import routers

#app_name = 'FormasDePagamento'
app_name = 'formapagamento'

router = routers.DefaultRouter()
#router.register('', views.formapagamentoViewSet, basename='formapagamentos')
router.register('', views.FormapagamentoViewSet, basename='formapagamentos')

urlpatterns = [
    path('', include(router.urls) )
]