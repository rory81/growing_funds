from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User

class Category(models.Model):
    """
    Content Project
    """
    class Meta: 
        verbose_name_plural="Categories"
    category = models.CharField(max_length=10 )

    def __str__(self):
        return self.category

class Project(models.Model):
    """
    Content Project
    """
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=90, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(max_length=5000)
    backers_story = models.TextField(max_length=5000)
    created_date = models.DateField(default=datetime.now)
    views = models.IntegerField(default=0)
    goal = models.IntegerField(default=0, blank=True, null=True)
    end_date = models.DateField(default=datetime.now, blank=True, null=True)
    num_days = models.IntegerField(default=0)
    raised = models.IntegerField(default=0)
    conditions = models.BooleanField(default= False, blank=False, null=False)


    def __str__(self):
        return self.title

