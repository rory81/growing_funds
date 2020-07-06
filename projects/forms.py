from django import forms
from .models import Project
from datetime import datetime

class StartProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        conditions = forms.BooleanField(widget=forms.CheckboxInput(attrs={'checked' : ''}), required=True)
        fields = ('title', 'image', 'category','description', 'backers_story', 'goal', 'end_date', 'conditions')
        labels = {
            "title":"Project Title",
            "image":"Project Image",
            "category":"Category",
            "description":"Project Description",
            "backers_story":"What's in it for the backers?",
            "goal":"Goal (USD)",
            "end_date":"Project End Date",
            "conditions": "I agree to the Terms and Conditions (see link in footer)"
        }
        


