from django.db import models
from django.utils import timezone
from datetime import datetime

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
    title = models.CharField(max_length=90)
    image = models.ImageField(upload_to="img", blank=False, null=False)
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(max_length=5000)
    backers_story = models.TextField(max_length=5000)
    created_date = models.DateField(default=datetime.now)
    views = models.IntegerField(default=0)
    goal = models.IntegerField(default=0)
    end_date = models.DateField(default=datetime.now)
    num_days = models.IntegerField(default=0)
    raised = models.IntegerField(default=0)


    def __str__(self):
        return self.title

