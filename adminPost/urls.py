from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^addDoctor', views.docAdd, name='addDoctor'),
	url(r'^doctorList', views.docList, name='doctorList'),
	url(r'^updateDoctor/(?P<pk>\d+)/$', views.update_doc, name='updateDoctor'),
	url(r'^deleteDoctor/(?P<pk>\d+)/$', views.delete_doc, name='deleteDoctor'),
]