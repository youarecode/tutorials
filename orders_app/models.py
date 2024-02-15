from django.db import models
from django.contrib.auth import get_user_model
from store_app.models import Product
from django.db.models import F, Sum, FloatField
# Create your models here.


User = get_user_model()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
    
    @property
    def total(self):
        return self.orderline_set.aggregate(
            total=Sum(F('price')*F('quantity'), output_field=FloatField())
        )['total']
    
    class Meta:
        db_table = 'orders'
        verbose_name = 'order'
        verbose_name_plural = 'orders'
        ordering = ['id']


class OrderLine(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    order       = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity    = models.IntegerField(default=1)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} units of {self.product.name}"
    
    class Meta:
        db_table = 'order_line'
        verbose_name = 'order line'
        verbose_name_plural = 'order lines'
        ordering = ['id']