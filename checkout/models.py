from django.db import models
import uuid  # to create order_number
from projects.models import Project
from django.conf import settings
from django_countries.fields import CountryField
from profiles.models import UserProfile

REWARDS = (
    ('Option 1', 'Option 1'),
    ('Option 2', 'Option 2'),
    ('Option 3', 'Option 3'),
    ('Nothing', 'Nothing'),
)

class Order(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country*', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, null=True, blank=False, on_delete=models.CASCADE)
    reward = models.CharField(max_length=9, choices=REWARDS, default="Nothing")
    amount_pledged = models.DecimalField(max_digits=100, decimal_places=2, null=False, default=1)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using uuid
        """
        return uuid.uuid4().hex.upper()


    def save(self, *args, **kwargs):
        """
        Override the original save method to set the ordernumber
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.order_number