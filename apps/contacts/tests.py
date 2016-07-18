from django.test import TestCase
from django.test import Client
from django.test import RequestFactory
from .models import Contact
from .models import RequestLog
from .contacts import RequestLoggingMiddleware
import datetime
import time
import types
import json


class ModelOneContactInstanceTestCase(TestCase):
    def setUp(self):
        c = Contact(
            name="Oliver",
            surname="Twist",
            bio="something lengthy I guess",
            jabber="jabber@jabber.com",
            skype="random",
            birthdate=datetime.date(2001, 10, 02),
            other_contacts="Phone: +1 100 472 4930\nFax: +1 300 474 4930\n"
        )
        c.save()

    def test_basic_contact_model(self):
        """
        Some very basic model test. There is only one contact instance in DB.
        """
        person = Contact.objects.filter(name="Oliver")[0]
        self.assertEqual(str(person), "Oliver Twist")
        self.assertTrue(isinstance(person, Contact))
        self.assertEqual(person.birthdate.year, 2001)
        other_contacts = person.other_contacts
        self.assertEqual(type(other_contacts), types.UnicodeType)
        self.assertTrue("Phone" in other_contacts)

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
        other_contacts = response.context['other_contacts']
        self.assertEqual(type(other_contacts[0]), types.ListType)
        self.assertEqual(type(other_contacts[0][0]), types.UnicodeType)
        self.assertEqual(len(other_contacts), 2)
        self.assertEqual(type(contact.bio), types.UnicodeType)


class NoContactInstancesInDBTestCase(TestCase):
    def test_no_contact_instances_in_db(self):
        """
        Test the case when there are no Contact instances in DB at all.
        The view will create an empty object and send it to context,
        but it will not save the object in the database.
        """
        response = Client().get('/')
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.context['contact'], None)
        with self.assertRaises(KeyError):
            response.context['other_contacts']
        self.assertFalse(Contact.objects.all())


class MultipleContactInstancesinDBTestCase(TestCase):
    def setUp(self):
        Contact.objects.create(
            name="First",
            surname="One",
            birthdate=datetime.date.today(),
        )
        Contact.objects.create(
            name="Second",
            surname="Two",
            birthdate=datetime.date.today(),
        )

    def test_multiple_contact_instances_in_db(self):
        """
        Test the case when there are multiple Contact instances in DB.
        The view will always select a first instance,
        since the database should have only 1 instance for now.
        """
        response = Client().get('/')
        self.assertEqual(200, response.status_code)
        contact = response.context['contact']
        self.assertEqual(str(contact), "First One")


class RequestViewTestCase(TestCase):
    def test_request_logs_view_get(self):
        """
        Test request_logs view with the response sent by GET method.
        Time variable is used for determining what requests to send.
        """
        response = Client().get('/requests/')
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'contacts/requests.html')
        self.assertEqual(type(response.context['time']), types.IntType)
        logs = response.context['request_logs']
        self.assertEqual(len(logs), 10)
        self.assertEqual(type(logs), types.ListType)
        self.assertEqual(type(logs[0]), types.StringType)

    def test_request_logs_view_post(self):
        """
        Test request_logs view with the response sent by AJAX POST method.
        """
        request_time = time.time() - 500
        response = Client().post(
            '/requests/',
            {'time': request_time},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest',
        )
        self.assertEqual(200, response.status_code)
        content = json.loads(response._container[0])
        self.assertGreater(content['time'], request_time)
        self.assertEqual(type(content['request_logs']), types.ListType)


class RequestLoggingMiddlewareTest(TestCase):
    def test_request_logging_middleware(self):
        """
        Test the middleware which will read the request data and save it.
        """
        factory = RequestFactory()
        logging_mw = RequestLoggingMiddleware()
        request = factory.get('/requests/')
        self.assertEqual(logging_mw.process_request(request), None)


class RequestLogModelTestCase(TestCase):
    def setUp(self):
        self.t = time.time()
        RequestLog.objects.create(
            method="GET",
            path="/",
            remote_addr="127.0.0.1",
            http_user_agent="Mozilla",
            username="myName",
            time=self.t,
        )

    def test_model_string_representation(self):
        entry = RequestLog.objects.first()
        self.assertEqual(str(entry), "myName GET Mozilla " + time.ctime(self.t))

    def test_middleware_to_database(self):
        Client().get("/")
        entry = RequestLog.objects.first()
        self.assertEqual(entry.path, '/')
        self.assertEqual(entry.method, 'GET')
        self.assertEqual(len(RequestLog.objects.all()), 2)
        Client().post("/requests/")
        self.assertEqual(len(RequestLog.objects.all()), 2)
