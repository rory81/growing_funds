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
)


class Project(models.Model):
    """
    Content Project
    """
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="img", blank=False, null=False, default="{% static 'img/main_logo_small.jpg' %}")
    category = models.CharField(max_length=9, choices=CATEGORIES)
    description = models.TextField(max_length=5000)
    backers_story = models.TextField(max_length=5000)
    created_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    goal = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    end_date = models.DateField(default=timezone.now)
    raised = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    percentage = models.DecimalField(max_digits=9, decimal_places=1, default=0)

    def __unicode__(self):
        return self.title

