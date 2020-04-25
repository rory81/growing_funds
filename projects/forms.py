from django import forms
from .models import Project

class StartProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'image', 'category','description', 'backer_story', 'goal', 'end_date')
