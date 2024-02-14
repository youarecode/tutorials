from django.http import HttpRequest
from store_app.models import Product

class Cart:
    def __init__(self, request:HttpRequest):
        self.request = request
        self.session = request.session

        cart = self.session.get('cart') # is there cart in this session?

        if not cart:
            cart = self.session['cart'] = {} #cart or self.cart??
        self.cart = cart
    
    def add(self, product:Product):
        if str(product.id) not in self.cart:
            self.cart[product.id] = {
                'product_id':product.id,
                'name':product.name,
                'price':str(product.price),
                'quantity':1,
                'image':product.image.url,
            }
        else:
            for key,value in self.cart.items():
                if key==str(product.id):
                    value['quantity'] +=1
                    value['price'] =  float(value['price'])+product.price
                    break
        
        self.save_cart()

    def save_cart(self):
        self.session['cart']  = self.cart
        self.session.modified = True

    def delete(self, product):
        product.id = str(product.id)
        if product.id in self.cart:
            del self.cart[product.id]
            self.save_cart()

    def decrease_product(self, product):
        for key, value in self.cart.items():
            if key == str(product.id):
                value['quantity'] -=1
                value['price'] = float(value['price'])-product.price
                if value['quantity'] < 1: self.delete(product)
                break
        self.save_cart()

    def clean_cart(self):
        self.session['cart']  = {}
        self.session.modified = True