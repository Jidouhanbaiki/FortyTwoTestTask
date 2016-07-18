from django.shortcuts import render
from .models import Contact
import time
import json

from django.http import HttpResponseBadRequest
from django.http import HttpResponse


def index(request):
    context = {}
    c = Contact.objects.first()
    if c:
        arr_other = c.other_contacts.strip().split("\n")
        context['other_contacts'] = [line.split(":") for line in arr_other]
    context['contact'] = c
    return render(request, "contacts/contact_detail.html", context)


def request_logs(request):

    if request.method == 'POST':
        if request.is_ajax():
            logs = [str(int(time.time() * 1000))[-6:] + " new data"
                    for i in range(2)]
            content = {
                'time': int(time.time() * 1000),
                'request_logs': logs,
            }

            return HttpResponse(
                json.dumps(content),
                content_type="application/json",
            )
        return HttpResponseBadRequest("Not implemented!")
    logs = [str(int(time.time()*1000))[-6:] + " init data" for i in range(10)]
    context = {
        'time': int(time.time() * 1000),
        'request_logs': logs,
    }
    return render(request, "contacts/requests.html", context)
