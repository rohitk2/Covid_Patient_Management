from django.db import models
from django.contrib.auth.models import User
import datetime

class Patient_Data(models.Model) :
    temperature = models.FloatField()
    pulse = models.FloatField()
    BloodOxygen = models.FloatField()
    BPSystolic = models.FloatField()
    BPDiastolic = models.FloatField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.timestamp)



