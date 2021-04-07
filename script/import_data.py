#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import json
from Patient_Management.models import Patient_Data
from django.contrib.auth.models import User
from datetime import datetime

import json
data1 = '{ "user":"user2", "Blood Pressure (Systolic)":100, "Blood Pressure (Diastolic)": 70, ' \
        '  "Pulse Rate":72, "Temperature":40, "Blood Oxygen":97}'
data1 = json.loads(data1)

#print(User.objects.all())

patient_username = data1["user"]
user_ = User.objects.filter(username=patient_username)[0]


data1 = Patient_Data(temperature=data1['Temperature'], 
                     pulse=data1["Pulse Rate"],
                     BloodOxygen=data1["Blood Oxygen"],
                     BPSystolic=data1["Blood Pressure (Systolic)"],
                     BPDiastolic=data1["Blood Pressure (Systolic)"],
                     timestamp=datetime.now(),
                     patient=user_)
print((data1.timestamp, data1.temperature))

data1.save()