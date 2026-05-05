from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    subject_name = models.CharField(max_length=200)

    def __str__(self):
        return self.subject_name


class StudyRecord(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    subject= models.ForeignKey(Subject, on_delete=models.CASCADE)
    hours = models.FloatField()
    date_studied = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.subject}-{self.hours}hrs"
    