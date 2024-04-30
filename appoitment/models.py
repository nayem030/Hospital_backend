from django.db import models
from doctor.models import Doctor, AvailableTime
from patient.models import Patient

APPOINMENT_STATUS=[
    ('Completed','Completed'),
    ('Running', 'Running'),
    ('Pending', 'pending'),
]

APPOINMENT_TYPE=[
    ('Offline','Offline'),
    ('Online', 'online'),
]

class Appointment(models.Model):
    patient= models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor= models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_type=models.CharField(choices=APPOINMENT_TYPE, max_length=10)
    appointment_status= models.CharField(choices=APPOINMENT_STATUS, max_length=20, default="Pending")
    symtomp= models.TextField()
    time = models.OneToOneField(AvailableTime, on_delete=models.CASCADE)
    cancel=models.BooleanField(default=False)
    
    def __str__(self):
        return f"Doctor : {self.doctor.user.first_name} Patient: {self.patient.user.first_name}"
    
    
