from django.test import TestCase
from django.test import Client

import datetime
import types
import time

from .models import Contact, Other


class ModelOtherTestCase(TestCase):
    def setUp(self):
        Other.objects.create(
            left="MyPhone",
            right="Some phone number"
        )

    def test_basic_Other(self):
        """
        A simple test for Other model which tests
        how the object is converted to string.
        """
        other = Other.objects.filter(left="MyPhone")[0]
        self.assertEqual(str(other), "MyPhone: Some phone number")


class ModelsTestCase(TestCase):
    def setUp(self):
        other1 = Other(
            left="Phone",
            right="Some phone number"
        )
        other1.save()
        other2 = Other(
            left="Second phone",
            right="Another phone number"
        )
        other2.save()
        c = Contact(
            name="Oliver",
            surname="Twist",
            bio="something lengthy I guess",
            jabber="jabber@jabber.com",
            skype="random",
            birthdate=datetime.date(2001, 10, 02)
        )
        c.save()
        c.other.add(other1)
        c.other.add(other2)
        c.save()

    def test_basic_contact_model(self):
        """
        Some very basic model test. Model is rather basic too, after all.
        """
        person = Contact.objects.filter(name="Oliver")[0]
        self.assertEqual(str(person), "Oliver Twist")
        self.assertTrue(isinstance(person, Contact))
        self.assertEqual(person.birthdate.year, 2001)
        self.assertEqual(len(person.other.all()), 2)
        other = person.other.filter(right="Some phone number")[0]
        self.assertEqual(other.left, "Phone")
        self.assertEqual(str(other), "Phone: Some phone number")

    def test_contacts_view(self):
        """
        Test the index view.
        """
        response = Client().get('/')
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'contacts/contact_detail.html')
        self.assertEqual(response.request['REQUEST_METHOD'], 'GET')
        self.assertEqual(Client().get('randompagename8787').status_code, 404)
        contact = response.context['contact']
        self.assertEqual(contact.name, 'Oliver')
        self.assertEqual(contact.surname, 'Twist')
        self.assertEqual(contact.birthdate, datetime.date(2001, 10, 2))
        self.assertEqual(contact.jabber, 'jabber@jabber.com')
        self.assertTrue(isinstance(contact.other.all()[0], Other))
        self.assertEqual(type(contact.bio), types.UnicodeType)


class RequestViewTestCase(TestCase):
    def test_request_logs_view_get(self):
        """
        Test request_logs view with the response sent by GET method.
        Time variable is used for determining what requests to send.
        """
        response = Client().get('request/')
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'contacts/requests.html')
        self.assertEqual(type(response.context['time']), types.StringType)
        logs = response.context['request_logs']
        self.assertEqual(len(logs), 10)
        self.assertEqual(type(logs), types.ListType)
        self.assertEqual(type(logs[0]), types.StringType)

    def test_request_logs_view_get(self):
        """
        Test request_logs view with the response sent by AJAX POST method.
        """
        request_time = time.time() - 500
        response = Client().post('request/', {'time': str(request_time)})
        self.assertGreater(response.context['time'], request_time)
        self.assertEqual(type(response.context['request_logs']), types.ListType)
        self.assertEqual(type(response.context['request_logs'][0]), types.StringType)
