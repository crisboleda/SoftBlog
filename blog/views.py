
from django.shortcuts import render


def contact(request):
    return render(request, template_name="core/contact.html")