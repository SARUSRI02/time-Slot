from django.db import models

# Create your models here.
from django.db import models

class Timeslot(models.Model):
    day = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject_name = models.CharField(max_length=100)
    faculty_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name