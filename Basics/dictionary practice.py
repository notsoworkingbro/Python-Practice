from random import choice

# prices = [120.50, 70.88, 22.19]
# products = ["Oil", "Marker", "Eraser"]
# dictionary = {}

# for i in range(len(prices)):
#     dictionary[products[i]] = prices[i]

# print(dictionary)

# # Alternative
# for product, price in zip(products, prices):
#     dictionary[product] = price

# print(dictionary)

# dictionary1 = {products[i]: prices[i] for i in range(len(prices))}
# dictionary2 = {product: price for product, price in zip(products, prices)}

# print(dictionary1)
# print(dictionary2)

# d = {
#     "a" : 1,
#     "b" : 2,
#     "c" : 3
# }

# z = d.keys()
# print(z)

# x = list(d.keys())
# print(x)

# v = d['a']
# print(v)

# b = d[choice(list(d.keys()))]
# print(d[choice(list(d.keys()))])

d2 = {
    "a" : (1, 1),
    "b" : (2, 5),
    "c" : (3, 10)
}

x, y = d2[choice(list(d2.keys()))]
print(x, y)