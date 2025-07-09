class Order :
    
    def __init__(self):
        self.carts = {}

    def cart_products(self) :
        if self.carts == {} :
            print('empty') 
            return  
        for product in self.carts :
            print(product.product_name,product.product_quantity,product.product_price)

    def pay_bill(self,seller) :
        
        sum = 0 
        for product in self.carts :
            sum += product.product_quantity * product.product_price
            seller_product = seller.menu.find_product(product.product_name) 
            if seller_product :
                if seller_product.product_quantity == product.product_quantity :
                    seller.menu.delete_product(product) 
                elif seller_product.product_quantity > product.product_quantity :
                    seller_product.product_quantity = seller_product.product_quantity - product.product_quantity 
            else : 
                print('Product in unavailable')
        self.clear_cart()
        print(f'Money {sum} taka was deduced from your wallet')
    



    def find_product(self,product_name) :
        for product in self.carts :
            if product.name.lower() == product_name :
                return product 
        return None 

    def add_product(self,product) :
        if product in self.carts :
            self.carts[product] += product.product_quantity 
        else :
            self.carts[product] = product.product_quantity 
    
    def remove_product(self,product) :
        if product in self.carts :
            del self.carts[product]
    
    def clear_cart(self) : 
        self.carts = {}

    