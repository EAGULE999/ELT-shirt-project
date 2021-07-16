from django.test import TestCase
from shop.models import Category, Subcategory, Product

class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='Men', slug='Men')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry_return(self):
        """
        Test Category model returns default name
        """
        data = self.data1
        self.assertEqual(str(data), 'Men')
