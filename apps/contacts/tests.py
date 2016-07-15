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
        self.assertTemplateUsed(response, 'contacts/index.html')
        self.assertEqual(response.request['REQUEST_METHOD'], 'GET')
        self.assertEqual(self.c.get('randompagename').status_code, 404)
