from django.shortcuts import render

BIO = "I studied Translation and obtained a second degree in Applied " \
    "Linguistics." \
    " I have recently graduated from the course in Applied Linguistics. " \
    "I guess it is not as cool as studying Computer Science or getting a " \
    "related degree initially, but at least I we had a couple of " \
    "Computational Linguistics related courses. "


def index(request):
    context = {
        'name': 'Andrii',
        'surname': 'Shatov',
        'birthdate': '17.01.1988',
        'bio': BIO,
        'email': 'andrii.shatov@gmail.com',
        'jabber': 'andrewshatov@42cc.co',
        'skype': 'parapheen',
        'other': [
            ['Phone number', '+380 97 735 5246'],
            ['Fax number', '+380 97 735 5246']
        ]
    }
    return render(request, "contacts/index.html", context)
