"""Serializer for file upload"""

from core.models import FileUpload, ProductionData
from rest_framework import serializers
from core.utilities import read_data


class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = "__all__"

    def create(self, validated_data):
        file = validated_data.get("file", None)
        read_data(file)
        obj = FileUpload.objects.create(**validated_data)
        return obj


class ProductionDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductionData
        fields = ["well_no", "oil", "gas", "brine"]
