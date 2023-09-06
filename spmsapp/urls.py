from django.urls import path
from . import views

app_name = 'spmsapp'

urlpatterns = [
    path('register_project_topic/', views.register_project_topic, name='register_project_topic'),
    path('project_topic_list/', views.project_topic_list, name='project_topic_list'),
]
