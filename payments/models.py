from django.db import models
from projects.models import Project

class Fund(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number= models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    amount = models.IntegerField(default=0, null=False)
    date = models.DateField()
    raised = models.IntegerField(default=0, null=False)
    project = models.OneToOneField(Project, default=1, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.full_name

