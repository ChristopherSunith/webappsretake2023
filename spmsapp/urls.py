from django.urls import path
from . import views

app_name = 'spmsapp'

urlpatterns = [
    path('register_project_topic/', views.register_project_topic, name='register_project_topic'),
    path('project_topic_list/', views.project_topic_list, name='project_topic_list'),
    path('select_project/', views.select_project, name='select_project'),
    path('manage_selections/', views.manage_selections, name='manage_selections'),
]
