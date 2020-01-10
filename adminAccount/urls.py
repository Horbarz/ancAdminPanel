from django.urls import path

from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	url(r'^login/$', auth_views.LoginView.as_view(template_name='adminAccount/login.html'), name='login'),
	# url(r'^register/$', views.register, name='register'),
]