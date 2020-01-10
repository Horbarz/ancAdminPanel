from django.urls import path

from .views import HomePageView, patientListView, errorView

urlpatterns = [
    path('',HomePageView.as_view(), name='admin-home'),
    path('patients/', patientListView.as_view(),name='patient-list'),
    path('error/',errorView.as_view(),name="error")
]