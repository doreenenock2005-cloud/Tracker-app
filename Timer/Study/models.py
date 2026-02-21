from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    subject_name = models.CharField(max_length=200)

    def __str__(self):
        return self.subject_name


class StudyRecord(models.Model):
    User= models.CharField(max_length=500)
    Subject= models.CharField(max_length=100)
    hours = models.FloatField()
    Date_Studied = models.DateField()
    created_at = models.DateTimeField()
    
    def __str__(self):
        return f"{self.user_name}"-"{self.Subject_name}"