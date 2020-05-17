from django import forms
from .models import Project
from payments.models import Fund
from datetime import datetime

class StartProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'image', 'category','description', 'backers_story', 'goal', 'end_date')
        labels = {
            "title":"Project Title",
            "image":"Project Image",
            "category":"Category",
            "description":"Project Description",
            "backers_story":"What's in it for the backers?",
            "goal":"Goal (USD)",
            "end_date":"Project End Date",
        }


