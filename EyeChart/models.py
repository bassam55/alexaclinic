from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_name = models.CharField(max_length=264)
    patient_age = models.DecimalField(max_digits=3,decimal_places=0)
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    AL_OS = models.CharField(max_length = 150, blank =True)
    AL_OD = models.CharField(max_length = 150, blank = True)
    AL_OU = models.CharField(max_length = 150, blank = True)

    H_OS = models.CharField(max_length = 150, blank =True)
    H_OD = models.CharField(max_length = 150, blank = True)
    H_OU = models.CharField(max_length = 150, blank = True)

    notes = models.TextField(blank = True)

    def __str__(self):
        return self.patient_name
