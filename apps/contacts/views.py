from django.shortcuts import render
from .models import Contact


def index(request):
    context = {}
    c = Contact.objects.all()[0]
    other_list = []
    for o in c.other.all():
        other_list.append(o.to_list())
    context['other'] = other_list
    context['contact'] = c
    return render(request, "contacts/contact_detail.html", context)
