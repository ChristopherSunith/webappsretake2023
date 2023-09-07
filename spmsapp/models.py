from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Supervisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='supervisor')


def get_default_supervisor():
    # Replace 'default_supervisor_username' with the username of your supervisor user.
    default_supervisor, created = Supervisor.objects.get_or_create(user=User.objects.get(username='user6'))
    return default_supervisor  # Return the ID of the default supervisor


class ProjectTopic(models.Model):
    name = models.CharField(max_length=255)
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_supervisor)

    def __str__(self):
        return self.name

    class Meta:  # This should be indented properly within the ProjectTopic class
        permissions = [
            ("view_spmsapp_projecttopic", "Can view project topic"),
        ]


class ProjectSelection(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='selected_projects')
    project = models.ForeignKey(ProjectTopic, on_delete=models.CASCADE)
    status = models.CharField(max_length=20,
                              choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')])

    def __str__(self):
        return f'{self.student} selected {self.project} proposed by {self.supervisor}'
