
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
import logging
import sys

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = request.user
            print(user)
            token = Token.objects.filter(user=user).delete()
            return Response({
                'message': 'Logout api worked well !!'
            }, status=status.HTTP_200_OK)
        except Exception as e:
            logging.error(str("line no {} error {}".format(
                sys.exc_info()[-1].tb_lineno, sys.exc_info())))
            return Response({'message': "Logout api stucked into exception!!",
                             'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
