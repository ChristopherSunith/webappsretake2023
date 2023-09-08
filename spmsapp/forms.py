from django import forms
from .models import ProjectTopic
from .models import ProjectSelection


class ProjectTopicForm(forms.ModelForm):
    class Meta:
        model = ProjectTopic
        fields = ['name']


class ProjectSelectionForm(forms.ModelForm):
    class Meta:
        model = ProjectSelection
        fields = ['project']