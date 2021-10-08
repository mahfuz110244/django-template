from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status


class HealthCheckAPI(APIView):
    permission_classes = (AllowAny, )

    def get(self, request: Request) -> Response:
        data = {
            'message': 'Django Template Service V1.',
            'method': str(self.request.method).lower(),
        }
        return Response(data={'data': data}, status=status.HTTP_200_OK)
