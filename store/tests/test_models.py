from django.test import TestCase
from store.models import Category, Product

class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='jango')

    def test_Category_moel_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Category))