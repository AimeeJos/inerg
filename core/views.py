from django.shortcuts import render
from rest_framework.parsers import FormParser, MultiPartParser
from core.models import FileUpload, ProductionData
from core.serializers import FileUploadSerializer, ProductionDataSerializer
from rest_framework import viewsets, filters, mixins
from django_filters.rest_framework import DjangoFilterBackend


class FileUploadView(viewsets.ModelViewSet):
    """Post api to upload xls file and data will be stored in database after calculating the total values of gas, oil and brine."""
    serializer_class = FileUploadSerializer
    queryset = FileUpload.objects.all()
    http_method_names = ['post']
    parser_classes = [MultiPartParser, FormParser]
    

class ProductionDataView(mixins.ListModelMixin, viewsets.GenericViewSet):
    """Get api to show total oil, gas and brine with filter based on well no."""
    serializer_class = ProductionDataSerializer
    queryset = ProductionData.objects.all()
    # http_method_names = ['get']
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = {
        'well_no': ['exact'],
    }
