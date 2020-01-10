from django.db import models

# Create your models here.

class DoctorPost(models.Model):
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    firstname = models.CharField(max_length=400, default=0)
    lastname = models.CharField(max_length=400, default=0)
    email = models.CharField(max_length=400, default=0)
    mobile = models.IntegerField(default=0)
    def __str__(self):
        return self.firstname
