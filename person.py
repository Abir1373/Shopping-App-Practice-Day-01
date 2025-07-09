from abc import ABC 
from menu import Menu 
from order import Order

class Person(ABC) :
    def __init__(self,name,email,password):
        self.name = name 
        self.email = email 
        self.password = password 
    
class Customer(Person) :
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.order = Order()

    def show_product(self,seller) :
        seller.menu.view_products() 

    def show_cart(self) :
        self.order.cart_products()

    def add_to_cart(self,product) :
        self.order.add_product(product)
        
        
class Seller(Person):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.menu = Menu()
    
     






    



    
