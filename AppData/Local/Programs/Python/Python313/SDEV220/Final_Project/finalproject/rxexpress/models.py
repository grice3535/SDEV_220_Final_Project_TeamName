from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    patientid = models.CharField(max_length=50, unique=True)
    last_appointment = models.DateField(null=True, blank=True)
    last_fill_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.patientid} {self.first_name} {self.last_name}"

class Prescription(models.Model):
   medication_ID = models.CharField(max_length=50, unique=True)
   medication_name = models.CharField(max_length=100)
   dosage = models.CharField(max_length=100)

   def __str__(self):
       return f"{self.medication_ID} for {self.patient.patientid}"

class RefillVerification:
    def __init__(self, patient: Patient, prescription:Prescription):
        self.patient_verification = f"Patient ID: {patient.patientid}, Name: {patient.first_name} {patient.last_name}, DOB: {patient.date_of_birth}"
        self.fk_patient_id=patient.patientid
        self.fk_medication_ID=prescription.medication_ID
        
    def __str__(self):
        return f"Refill Verification for {self.patient_verification}, Medication: {self.fk_medication_ID}"
        f"(Patient = {self.fk_patient_id}, Medication = {self.fk_medication_ID})"