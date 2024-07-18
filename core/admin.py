from django.contrib import admin
from core.models import FileUpload, ProductionData

tables = (
    FileUpload, ProductionData
)
for table in tables:
    admin.site.register(table)