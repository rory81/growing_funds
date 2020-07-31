from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User


def one_month_from_today():
    return datetime.now() + timedelta(days=30)


class Category(models.Model):
    """
    Content Project
    """
    class Meta:
        verbose_name_plural = "Categories"
    category = models.CharField(max_length=10)

    def __str__(self):
        return self.category


class Project(models.Model):
    """
    Content Project
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=90, blank=False, null=False)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    category = models.ForeignKey('Category', blank=False, null=True, on_delete=models.SET_NULL)
    description = models.TextField(max_length=5000)
    backers_story_option1 = models.TextField(max_length=5000, null=False, blank=False)
    backers_story_option2 = models.TextField(max_length=5000, null=False, blank=False)
    backers_story_option3 = models.TextField(max_length=5000, null=False, blank=False)
    created_date = models.DateField(default=datetime.now, editable=False)
    views = models.IntegerField(default=0)
    goal = models.IntegerField(default=0)
    end_date = models.DateField(default=one_month_from_today)
    num_days = models.IntegerField(default=0)
    raised = models.IntegerField(default=0)
    conditions = models.BooleanField(default=False, choices=[(True, 'Yes'), (False, 'No')], null=True, blank=False)


    def __str__(self):
        return self.title
