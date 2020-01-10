from rest_framework.serializers import (
	ModelSerializer,
)

from adminPost.models import DoctorPost


class listDoctorSerializer(ModelSerializer):
    class Meta:
        model = DoctorPost
        fields = [
            'id',
            'firstname',
            'lastname',
            'email',
            'mobile'
        ]


class addDoctorSerializer(ModelSerializer):
    class Meta:
        model = DoctorPost
        fields = [
            'firstname',
            'lastname',
            'email',
            'mobile',
        ]

class deleteDoctorSerializer(ModelSerializer):
	class Meta:
		model = DoctorPost
		fields = [
			'id',
        ]

class updateDoctorSerializer(ModelSerializer):
	class Meta:
		model = DoctorPost
		fields = [
			'firstname',
            'lastname',
            'email',
            'mobile',
        ]
