from django.db import models
from projects.models import Project
from django.utils import timezone
from datetime import datetime

class Fund(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number= models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    donation = models.IntegerField(default=0, null=False)
    date = models.DateField(default=datetime.now)
    raised = models.IntegerField(default=0, null=False)
    project = models.ForeignKey(Project, default=1, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.full_name
