from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "adminPanel/home.html"

class patientListView(TemplateView):
    template_name = "adminPanel/patient_list.html"

class errorView(TemplateView):
    template_name = "adminPanel/404.html"

