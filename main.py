from product import *
from person import * 

seller1 = Seller('Abir','abir@gmail.com','123455')
customer = Customer('Mahdi','mahdi@gmail.com','123456')

seller1.menu.add_product(Product('chocolate',12,100)) 

customer.show_product(seller1)
customer.add_to_cart(Product('chocolate',7,100))
customer.show_cart()


customer.order.pay_bill(seller1)
customer.show_product(seller1)
customer.show_cart()
