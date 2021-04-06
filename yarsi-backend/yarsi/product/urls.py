from .api.product import ProductApiView
from django.urls import path
from . import views

urlpatterns = [
    path('product_list/', ProductApiView.as_view()),


]
