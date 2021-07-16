from unittest import skip

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpRequest

from shop.models import Category, Subcategory, Product
from shop.views import all_products

@skip("demonstrating skipping")
class TestSkip(TestCase):
    def test_skip_example(self):
        pass


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        User.objects.create(username='admin')
        Category.objects.create(name='Men', slug='men')
        Subcategory.objects.create(category_id=1, name='T-shirt', slug='T-shirt', created_by_id=1)
        Product.objects.create(category_id=1, subcategory_id=1, name='Black T-shirt', created_by_id=1,
                               slug='black-t-shirt', price='20.00', image='Black T-shirt')

    def test_url_allowed_hosts(self):
        """
        Test homepage response status
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test products response status
        """
        response = self.c.get(
            reverse('product_detail', args=['black-t-shirt']))
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test subcategory response status
        """
        response = self.c.get(
            reverse('subcategory_list', args=['T-shirt']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        """
        Example: code validation, search HTML for text
        """
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Home</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
