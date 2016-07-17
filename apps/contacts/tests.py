from django.test import TestCase
from django.test import Client
from .models import Contact, Other
import datetime
import types


class ModelsTestCase(TestCase):
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
        Some very basic model test. Model is rather basic too, after all.
        """
        person = Contact.objects.filter(name="Oliver")[0]
        self.assertEqual(str(person), "Oliver Twist")
        self.assertTrue(isinstance(person, Contact))
        self.assertEqual(person.birthdate.year, 2001)
        other_contacts = person.other_contacts
        self.assertEqual(type(other_contacts), types.StringType)
        self.assertTrue("Phone" in other_contacts)

    def test_contacts_view(self):
        """
        Test all views in this app.
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
        self.assertEqual(type(other_contacts[0][0]), types.StringType)
        self.assertEqual(len(other_contacts), 2)
        self.assertEqual(type(contact.bio), types.UnicodeType)
