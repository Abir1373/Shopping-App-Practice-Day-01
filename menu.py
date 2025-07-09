class Menu :
    
    def __init__(self):
        self.products = []

    def add_product(self,product) :
        self.products.append(product) 
    
    def find_product(self,product_name) :
        for product in self.products :
            if product.product_name.lower() == product_name :
                return product 
        return None 
    
    def delete_product(self,customer_product) :
        for product in self.products :
            if product.product_name.lower() == customer_product.product_name.lower() :
                self.products.remove(product)  

    def view_products(self) :
        for product in self.products :
            print(product.product_name , product.product_quantity,product.product_price) 

    