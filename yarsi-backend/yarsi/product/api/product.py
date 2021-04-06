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
from ..models import Product


class ProductApiView(APIView):

    @swagger_auto_schema(
        operation_description="product API , Authentication not Required !!",
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
                    "message": "product api worked well!!",
                }
            )
        },
    )
    def post(self, request, *args, **kwargs):
        try:
            product = Product.objects.all()
            payload = []
            for i in product:
                dict1 = {}
                dict1["id"] = i.id
                dict1["name"] = i.name 
                dict1["price"] = i.price
                dict1["size"] = i.size
                dict1["color"] = i.color
                dict1["category"] = i.category.title
                dict1["matrial"] = i.material
                dict1["count"] = i.count

                payload.append(dict1)

            return Response({
                'data' : payload,
                'message': 'product api worked well !!'
            }, status=status.HTTP_200_OK)
        except Exception as e:
            logging.error(str("line no {} error {}".format(
                sys.exc_info()[-1].tb_lineno, sys.exc_info())))
            return Response({'message': "product api stucked into exception!!",
                             'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
