import logging
import sys
from customer.models import Customer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User


class Signup(APIView):

    @swagger_auto_schema(
        operation_description="User Loan Detail Registration API , Authentication Required !!",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "email": openapi.Schema(type=openapi.TYPE_STRING),
                "password": openapi.Schema(type=openapi.TYPE_STRING),
                "first_name": openapi.Schema(type=openapi.TYPE_STRING),
                "last_name": openapi.Schema(type=openapi.TYPE_STRING),
                "gender": openapi.Schema(type=openapi.TYPE_STRING),
                "phone_number": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={
            200: str(
                {
                    "message": "Signup api worked well!!",
                }
            )
        },
    )
    def post(self, request):
        try:
            data = request.data
            print(data["phone_number"])
            user_instance = User.objects.filter(email=data["email"]).first()
            if user_instance:
                return Response({
                    'error': 'User Already Registered !!',
                }, status=status.HTTP_400_BAD_REQUEST)
            else:
                create_user = User.objects.create_user(
                    username=data["email"],
                    email=data["email"],
                    password=data["password"],
                    first_name=data["first_name"],
                    last_name=data["last_name"],
                    is_staff=False,
                    is_active=True

                )
                Customer.objects.create(user=create_user,gender=data["gender"],phone_number=data['phone_number']).save()
            return Response({
                            'message': 'Signup api worked well !!',
                            }, status=status.HTTP_200_OK)

        except Exception as e:
            logging.error(str("line no {} error {}".format(
                sys.exc_info()[-1].tb_lineno, sys.exc_info())))
            return Response({'message': "Signup api stucked into exception!!",
                             'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
