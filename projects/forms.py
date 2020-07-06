from django import forms
from .models import Project
from datetime import datetime



class StartProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'image', 'category','description', 'backers_story', 'goal', 'end_date', 'conditions' )
        labels = {
            "title":"Project Title",
            "image":"Project Image",
            "category":"Category",
            "description":"Project Description",
            "backers_story":"What's in it for the backers?",
            "goal":"Goal (USD)",
            "end_date":"Project End Date",
            "conditions": "Agree to Terms & Conditions?"
        }
        
    def clean_conditions(self):
        conditions = self.cleaned_data.get('conditions')
        if conditions == False:
            raise forms.ValidationError('Please agree to our terms and conditions')
        return conditions



        


