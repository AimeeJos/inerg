from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import FileUpload, ProductionData


class ProductionDataModelTest(TestCase):
    def test_production_data_creation(self):
        production_data = ProductionData.objects.create(
            well_no="W123", oil=100, gas=200, brine=300
        )

        # Check if the fields are set correctly
        self.assertEqual(production_data.well_no, "W123")
        self.assertEqual(production_data.oil, 100)
        self.assertEqual(production_data.gas, 200)
        self.assertEqual(production_data.brine, 300)

    def test_production_data_blank_fields(self):
        production_data = ProductionData.objects.create()

        # Check if the blank fields are allowed
        self.assertIsNone(production_data.well_no)
        self.assertIsNone(production_data.oil)
        self.assertIsNone(production_data.gas)
        self.assertIsNone(production_data.brine)

    def test_production_data_nullable_fields(self):
        production_data = ProductionData.objects.create(
            well_no=None, oil=None, gas=None, brine=None
        )

        # Check if the nullable fields are allowed
        self.assertIsNone(production_data.well_no)
        self.assertIsNone(production_data.oil)
        self.assertIsNone(production_data.gas)
        self.assertIsNone(production_data.brine)

    def test_production_data_default_values(self):
        production_data = ProductionData.objects.create()

        # Check if the default values are None
        self.assertIsNone(production_data.well_no)
        self.assertIsNone(production_data.oil)
        self.assertIsNone(production_data.gas)
        self.assertIsNone(production_data.brine)
        
        
            
class ProductionDataAPITest(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a ProductionData instance
        self.production_data = ProductionData.objects.create(
            well_no='34059243520000',
            oil=55,
            gas=122711,
            brine=369
        )

    def test_get_production_data(self):
        response = self.client.get('/production/', {'well_no': '34059243520000'})
        
        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check if the response content is correct
        expected_data = [
            {
                "well_no": "34059243520000",
                "oil": 55,
                "gas": 122711,
                "brine": 369
            }
        ]
        self.assertJSONEqual(response.content, expected_data)


