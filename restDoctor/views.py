from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.generics import (
	RetrieveUpdateAPIView,
	DestroyAPIView,
	ListAPIView
	)

from rest_framework.generics import (CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView)
from rest_framework.response import Response
from django.http import JsonResponse

from .serializers import listDoctorSerializer
from .serializers import addDoctorSerializer
from .serializers import deleteDoctorSerializer
from .serializers import updateDoctorSerializer

from rest_framework.response import Response

from adminPost.models import DoctorPost

from rest_framework.permissions import (
	IsAuthenticated,
	IsAuthenticatedOrReadOnly,
	)

from .permissions import IsOwnerOrReadOnly



from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication



class ListDoctorAPIView(ListAPIView):
	serializer_class = listDoctorSerializer
	queryset = DoctorPost.objects.all()


class AddDoctorAPI(CreateAPIView):
	# authentication_classes = (TokenAuthentication, SessionAuthentication)
	# permission_classes = (IsAuthenticated,)
	serializer_class = addDoctorSerializer
	queryset = DoctorPost.objects.all()

	def perform_create(self, serializer):
		serializer.save()
		# serializer.save(author = self.request.user.id)

class DeleteDoctorAPI(DestroyAPIView):
	queryset = DoctorPost.objects.all()
	serializer_class = deleteDoctorSerializer
	lookup_field = 'id'
	# permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
	# authentication_classes = (TokenAuthentication, SessionAuthentication)

class UpdateDoctorAPI(RetrieveUpdateAPIView):
	queryset = DoctorPost.objects.all()
	serializer_class = updateDoctorSerializer
	lookup_field = 'id'
	# permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
	# authentication_classes = (TokenAuthentication, SessionAuthentication)

