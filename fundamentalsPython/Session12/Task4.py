products = ['Mobile', 'Mouse', 'Laptop', 'Monitor', 'Keyboard']

result = list(filter(lambda name: name.startswith('M'), products))

print("Products starting with M:", result)