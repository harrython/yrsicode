from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	gender = models.CharField(max_length=1, null=True)
	phone_number= models.CharField(max_length=10)

# data = request.data
# a = Product.objects.filter(id=data['product_id']).first()

# if a:
# 	Cart.objects.create(user = request.user, product = a).save()
class Cart(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
