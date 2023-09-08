from django.http import HttpResponse
from .forms import ProjectTopicForm
from .models import ProjectTopic
from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, redirect
from .forms import ProjectSelectionForm
from .models import ProjectSelection


# Create your views here.

def home(request):
    return render(request, 'spmsapp/home.html')


def register_project_topic(request):
    if request.method == 'POST':
        form = ProjectTopicForm(request.POST)
        # Check if the user has the supervisor or administrator role
        if request.user.role in ['supervisor', 'administrator']:
            project_topic = form.save(commit=False)
            project_topic.supervisor = request.user
            project_topic.save()
            return redirect('spmsapp:project_topic_list')
        else:
            return HttpResponse("Permission denied. Only supervisors and administrators can register project topics.")

    else:
        form = ProjectTopicForm()
    return render(request, 'spmsapp/register_project_topic.html', {'form': form})


def project_topic_list(request):
    project_topics = ProjectTopic.objects.all()

    # Check if the user's role is 'supervisor' or 'administrator'
    is_supervisor_or_admin = request.user.role in ['supervisor', 'administrator']

    return render(request, 'spmsapp/project_topic_list.html',
                  {'project_topics': project_topics, 'is_supervisor_or_admin': is_supervisor_or_admin})


def select_project(request):
    if request.method == 'POST':
        form = ProjectSelectionForm(request.POST)
        if form.is_valid():
            project = form.cleaned_data['project']
            student = request.user  # Assuming the logged-in user is the student
            supervisor = project.supervisor  # Get the supervisor for the selected project
            ProjectSelection.objects.create(project=project, student=student, supervisor=supervisor, status='Pending')
            return redirect('spmsapp:project_topic_list')  # Redirect to the project list after selection
    else:
        form = ProjectSelectionForm()
    return render(request, 'spmsapp/select_project.html', {'form': form})


def manage_selections(request):
    # Get all project selections with status 'Pending' for the current supervisor
    selections = ProjectSelection.objects.filter(supervisor=request.user, status='Pending')

    if request.method == 'POST':
        # Handle the form submission for accepting/rejecting selections
        form = ProjectSelectionForm(request.POST)
        if form.is_valid():
            selection_id = form.cleaned_data['selection_id']
            selection = ProjectSelection.objects.get(id=selection_id)
            action = form.cleaned_data['action']

            # Check if the selection belongs to the current supervisor
            if selection.supervisor == request.user:
                if action == 'accept':
                    selection.status = 'Accepted'
                    selection.save()
                elif action == 'reject':
                    selection.status = 'Rejected'
                    selection.save()
            else:
                return HttpResponse("Permission denied")

    else:
        form = ProjectSelectionForm()

    return render(request, 'spmsapp/manage_selections.html', {'selections': selections, 'form': form})
