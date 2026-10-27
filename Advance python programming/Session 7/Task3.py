class ZomatoOrder:
    def add_item(self,items,quantity = 1):
        print("item :",items)
        print("Quantity :",quantity)

obj = ZomatoOrder()
obj.add_item("Pizza")
print()
obj.add_item("Burger",3)        