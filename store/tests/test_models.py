from django.db.models.fields import SlugField
from django.test import TestCase
from store.models import Category, Product

class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='Shorts', slug='Shorts')

    def test_Category_moel_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Category))
    
    def test_Category_model_entry(self):
        data = self.data1
        self.assertEqual(str(data), 'Shorts')
    
class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name='Shorts', Slug='Shorts')
        self.data1 = Product.objects.create(category_id=1, title='Shorts one', slug='Shorts one', price='35.00', description='New shorts')

    def Test_products_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'Shorts one')
