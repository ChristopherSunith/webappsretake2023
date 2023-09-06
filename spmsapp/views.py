from django.shortcuts import render, redirect
from .forms import ProjectTopicForm
from .models import ProjectTopic
from django.contrib.auth.decorators import permission_required


# Create your views here.


def register_project_topic(request):
    if request.method == 'POST':
        form = ProjectTopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('spmsapp:project_topic_list')
    else:
        form = ProjectTopicForm()
    return render(request, 'spmsapp/register_project_topic.html', {'form': form})


def project_topic_list(request):
    project_topics = ProjectTopic.objects.all()
    return render(request, 'spmsapp/project_topic_list.html', {'project_topics': project_topics})
