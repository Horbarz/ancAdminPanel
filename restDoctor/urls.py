from restDoctor import views
from django.conf.urls import url

urlpatterns = [
	url(r'^list/$', views.ListDoctorAPIView.as_view(), name='restdoctor-list'),
	url(r'^add/$', views.AddDoctorAPI.as_view(), name='restdoctor-add'),
    url(r'^delete/(?P<id>[\w-]+)/$', views.DeleteDoctorAPI.as_view(), name='restdoctor-delete'),
    url(r'^edit/(?P<id>[\w-]+)/$', views.UpdateDoctorAPI.as_view(), name='restdoctor-edit'),
]