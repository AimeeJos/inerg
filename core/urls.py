from django.urls import path,include
from rest_framework import routers
from core import views
router = routers.DefaultRouter()
router.register('upload', views.FileUploadView)
router.register('production', views.ProductionDataView)

urlpatterns = [
    path('', include(router.urls)),
]