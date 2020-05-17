from django.contrib import admin
from .models import Fund
"""
try StackedInline instead of TabularInline, to see what you like most
"""
admin.site.register(Fund)
    
