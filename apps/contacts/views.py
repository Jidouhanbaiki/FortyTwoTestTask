from django.shortcuts import render
from .models import Contact


def index(request):
    context = {}
    c = Contact.objects.first()
    if c:
        arr_other = c.other_contacts.strip().split("\n")
        context['other_contacts'] = [line.split(":") for line in arr_other]
    context['contact'] = c
    return render(request, "contacts/contact_detail.html", context)
