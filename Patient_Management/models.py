from django.db import models
from django.contrib.auth.models import User

class Patient_Data(models.Model) :
    temperature = models.FloatField()
    pulse = models.FloatField()
    BloodOxygen = models.FloatField()
    BPSystolic = models.FloatField()
    BPDiastolic = models.FloatField()
    patient = models.ForeignKey(User, on_delete=models.CASCADE)

    #def __str__(self) :
    #    return self.patient



