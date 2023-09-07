# Generated by Django 4.2.4 on 2023-09-06 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import spmsapp.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spmsapp', '0005_alter_supervisor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecttopic',
            name='supervisor',
            field=models.ForeignKey(default=spmsapp.models.get_default_supervisor, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
