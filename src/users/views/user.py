from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

import logging

logger = logging.getLogger('django_template')

from users.serializers import (
    UserDetailSerializer
)


class UserDetailsView(generics.RetrieveUpdateAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
