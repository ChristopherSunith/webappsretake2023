from django.db import models


# Create your models here.

class ProjectTopic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:  # This should be indented properly within the ProjectTopic class
        permissions = [
            ("view_spmsapp_projecttopic", "Can view project topic"),
        ]
