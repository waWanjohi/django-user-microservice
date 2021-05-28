from django.db import models
from django.db.models import fields
from users.models import NewUser
from rest_framework import serializers


class NewUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewUser
        fields = ('email', 'user_name', 'first_name', 'last_name',
                  'phone_number', 'start_date', 'is_staff', 'is_active')
