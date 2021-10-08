import datetime

from dateutil import parser, tz
from django.contrib.auth.models import AbstractBaseUser, User, UserManager
from rest_framework import serializers


class UserDetailSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('email', 'phone', 'title', 'gender')

    def validate_date_of_birth(self, value):
        dob = self.initial_data.get('date_of_birth')
        if datetime.datetime.utcnow().astimezone(tz.gettz('UTC')).date() <= parser.parse(dob).astimezone(tz=tz.gettz('UTC')).date():
            raise serializers.ValidationError({
                'date_of_birth': 'Future or current date not allowed',
            })
        return value