class Cake:
    def __init__(self,cake_id,flavor,size,quantity,price) :
        self.cake_id = cake_id
        self.flavor = flavor
        self.size = size
        self.quantity = quantity
        self.price = price

    def __str__(self):
        data = (f"CakeId : {self.cake_id},Flavor: {self.flavor},Size: {self.size},Price: {self.price}")
        return data
        
    