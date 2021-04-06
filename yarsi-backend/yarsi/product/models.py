from django.db import models

# Create your models here.

class Category(models.Model):
	title = models.CharField(max_length=200)

class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField()
	count = models.IntegerField(default=1,null=True, blank=True)
	image = models.ImageField(null=True, blank=True)
	size = models.CharField(max_length=200)
	color = models.CharField(max_length=200)
	material=models.CharField(max_length=200)
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)






# class Order(models.Model):
# 	user_Id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
# 	date_ordered = models.DateTimeField(auto_now_add=True)
# 	product_Id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)

	