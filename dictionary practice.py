prices = [120.50, 70.88, 22.19]
products = ["Oil", "Marker", "Eraser"]
dictionary = {}

for i in range(len(prices)):
    dictionary[products[i]] = prices[i]

print(dictionary)

# Alternative
for product, price in zip(products, prices):
    dictionary[product] = price

print(dictionary)

dictionary1 = {products[i]: prices[i] for i in range(len(prices))}
dictionary2 = {product: price for product, price in zip(products, prices)}

print(dictionary1)
print(dictionary2)