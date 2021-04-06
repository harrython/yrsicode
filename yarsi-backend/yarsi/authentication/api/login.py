from rest_framework.authtoken.views import ObtainAuthToken
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


class Login(ObtainAuthToken):

    @swagger_auto_schema(
        operation_description="Login API , Authentication not Required !!",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "username": openapi.Schema(type=openapi.TYPE_STRING),
                "password": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={
            200: str(
                {
                    "message": "Login api worked well!!",
                }
            )
        },
    )
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data,
                                               context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.email,
                'message': 'Login api worked well !!'
            }, status=status.HTTP_200_OK)
        except Exception as e:
            logging.error(str("line no {} error {}".format(
                sys.exc_info()[-1].tb_lineno, sys.exc_info())))
            return Response({'message': "Login api stucked into exception!!",
                             'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
