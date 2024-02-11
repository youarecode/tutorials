from django.db import models

# Create your models here.

class Clients(models.Model):
    name=models.CharField(max_length=30)
    address = models.CharField(max_length=50, verbose_name='The address')
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.name


class Article(models.Model):
    name=models.CharField(max_length=30)
    category=models.CharField(max_length=20)
    price=models.IntegerField()

    def __str__(self):
        return f"Name is {self.name}, the category is {self.category} and the price is {self.price}"
    
class Orders(models.Model):
    number = models.IntegerField()
    date = models.DateField()
    delivered = models.BooleanField()