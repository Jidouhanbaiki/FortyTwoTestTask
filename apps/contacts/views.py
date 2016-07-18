from django.shortcuts import render
from .models import Contact
import datetime
import time

from django.http import HttpResponseBadRequest


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


def request_logs(request):
    if request.method == 'POST':
        return HttpResponseBadRequest("Not implemented!")

    logs = [str(int(time.time()*1000))[-6:] + " init data" for i in range(10)]
    print logs[0]
    context = {
        'time': int(time.time() * 1000),
        'request_logs': logs,
    }
    return render(request, "contacts/requests.html", context)
