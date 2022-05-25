from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)    
    shape = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    price = models.FloatField() 

    def __str__(self):
        return str(self.id)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    address = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

class Recommendation(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)