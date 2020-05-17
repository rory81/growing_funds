from django.db import models
from projects.models import Project

class Fund(models.Model):
    project = models.ForeignKey(Project, null=False, default=1)
    full_name = models.CharField(max_length=50, blank=False)
    phone_number= models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    amount = models.IntegerField(default=0, null=False)
    date = models.DateField()

    def __str__(self):
        return "{0} {1} {2} {3} {4}".format(self.id, self.project.title, self.date, self.full_name, self.amount)

