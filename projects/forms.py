from django import forms
from .models import Project
from datetime import datetime, timedelta



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
    
    def clean_goal(self):
        goal = self.cleaned_data.get('goal')
        if goal == 0:
            raise forms.ValidationError('Please enter a goal amount higher than 0')
        return goal
    
    def clean_end_date(self):
        end_date = self.cleaned_data.get('end_date')
        if (end_date - datetime.now().date()).days < 30:
            raise forms.ValidationError('The duration of a project should be at least 30 days')
        return end_date





        


