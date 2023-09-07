from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    password = models.CharField(max_length=100)  # hashed password is implements in views
    role = models.CharField(max_length=20)  # Administrator, Supervisor, Student

    # Add the is_staff field
    is_staff = models.BooleanField(default=False)

    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    USERNAME_FIELD = 'username'

    # Make is_anonymous and is_authenticated properties
    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True

    # Define other methods and properties as needed

    # Override the save method to store role in lowercase
    def save(self, *args, **kwargs):
        self.role = self.role.lower()  # Convert role to lowercase
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username  # Return the username as the string representation
