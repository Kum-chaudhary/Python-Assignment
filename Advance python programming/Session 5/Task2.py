class FoodOrder:
    def __init__(self,Restaurant_name,items,total_price):
        self.Restaurant_name = Restaurant_name
        self.items = items
        self.total_price = total_price

    def show_order(self):
        print("Restaurant :",self.Restaurant_name)
        print("items :",",".join(self.items))
        print("total_price :Rs.",self.total_price) 

order = FoodOrder("Pizza Hut",["Pizza","Garlic Bread","Cold Drink"],550)
order.show_order()