from django.db import models
import uuid  # to create order_number
from projects.models import Project
from django.contrib.auth.models import User
from django.conf import settings

class Order(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE) 
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    project_number = models.ForeignKey(Project, null=False, blank=False, on_delete=models.CASCADE)
    reward = models.CharField(max_length=100, null=False, blank=False)
    amount_pledged = models.DecimalField(max_digits=100, decimal_places=2, null=False, default=0)

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