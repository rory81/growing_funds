from django.db import models
from django.utils import timezone

CATEGORIES = (
    ('ARTS','Arts'),
    ('CHAR','Charity'),
    ('FILM','Film'),
    ('FOOD','Food'),
    ('GAME','Games'),
    ('MUSE', 'Music'),
    ('PUBL', 'Publishing'),
    ('TECH','Technology'),
    ('MISC', 'Miscellaneous'),
)


class Project(models.Model):
    """
    Content Project
    """
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="img")
    category = models.CharField(max_length=9, choices=CATEGORIES, default="MISC")
    description = models.TextField()
    backer_story = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    goal = models.IntegerField(default=0)
    end_date = models.DateField()

    def __unicode__(self):
        return self.title

