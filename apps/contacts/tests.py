from django.test import TestCase
from django.test import Client

class ViewsTestCase(TestCase):
    def setUp(self):
        self.c = Client()
        pass


    def test_contacts_view(self):
        """
        Test all views in this app.
        """
        response = self.c.get('/')
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'index.html')
        self.assertEqual(response.method, 'GET')
        self.assertEqual(self.c.get('randompagename').status_code, 404)



class SomeTests(TestCase):
    def test_math(self):
        "put docstrings in your tests"
        assert(2 + 2 == 4)
