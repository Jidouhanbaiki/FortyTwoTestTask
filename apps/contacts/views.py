from django.shortcuts import render
from .models import Contact
import datetime


def index(request):
    context = {}
    all_contacts = Contact.objects.all()
    if all_contacts:
        c = all_contacts[0]
    else:
        # I do not save this object to keep the DB clean
        c = Contact(
            name="",
            surname="",
            birthdate=datetime.date.today()
        )
    arr_other = c.other_contacts.strip().split("\n")
    context['other_contacts'] = [line.split(":") for line in arr_other]
    context['contact'] = c
    return render(request, "contacts/contact_detail.html", context)
