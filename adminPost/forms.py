from django import forms
from adminPost.models import DoctorPost


class AddDoctorForm(forms.ModelForm):
    class Meta:
        model = DoctorPost
        exclude = ('author', )


class DoctorList(forms.ModelForm):
    class Meta:
        model = DoctorPost
        exclude = [""]


class UpdateDoctorForm(forms.ModelForm):
    class Meta:
        model = DoctorPost
        exclude = ('author',)

