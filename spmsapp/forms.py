from django import forms
from .models import ProjectTopic


class ProjectTopicForm(forms.ModelForm):
    class Meta:
        model = ProjectTopic
        fields = ['name']

