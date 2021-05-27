from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

"""
The user Manager is required for a custom user, 
Here I've defined all the checks to create a user and a SuperUser
"""


class CustomAccountManager(BaseUserManager):
    """ A function to create a superuser """

    def create_superuser(self, email, user_name, first_name, last_name, phone_number, password, **other_fields):

        # Set the superuser fields to true
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        """
        The following if statements perform a simple check to confirm the Inserted fields work as expected.
        This is not necessary for the function to work, so you can remove to ensure conventional function best practice.
        """
        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, last_name, phone_number, password, **other_fields)

    def create_user(self, email, user_name, first_name, last_name, phone_number, password, **other_fields):

        """
        The following if statements perform a simple check to confirm the Inserted fields work as expected.
        This is not necessary for the function to work, so you can remove to ensure conventional function best practice.
        """
        if not email:
            raise ValueError(_('You must provide an email address'))

        if not phone_number:
            raise ValueError(_('Please enter your phone Number to continue'))

        if not user_name:
            raise ValueError(_('You need to provide a user_name'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, last_name=last_name, phone_number=phone_number, **other_fields)
        user.set_password(password)
        user.save()
        return user


"""
A custom User model that overrides the default Django user Model
For more details on how to work with the AbstractBaseUser and BaseUser, please visit the Django documentation here:
https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#specifying-custom-user-model
"""


class NewUser(AbstractBaseUser, PermissionsMixin):
    # The new user attributed.

    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=100, unique=True)  # NOTE: This will also be the handle
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    phone_number = models.IntegerField(unique=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    # Specify the user manager
    objects = CustomAccountManager()

    # And of course the desired field for user_name, and then the required fields
    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'phone_number']

    # Add a friendly identifier on the admin page for each NewUser object
    def __str__(self):
        name_tag = self.first_name + ' ' + self.last_name
        return name_tag
