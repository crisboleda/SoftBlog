
from django.shortcuts import render
from django.views.generic import ListView, TemplateView


class ContactView(TemplateView):
    template_name = 'core/contact.html'


