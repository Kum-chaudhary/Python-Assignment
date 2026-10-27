names = ["Shoes","bags","Headphones","watch"]

prices = [1000,700,1200,2200]

products = [(name,price) for name, price in zip(names,prices) if price > 1000]

print(products)