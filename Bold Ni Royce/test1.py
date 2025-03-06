from random import choice

d = {
    "a" : 1,
    "b" : 2,
    "c" : 3
}

z = d.keys()
print(z)

x = list(d.keys())
print(x)

v = d['a']
print(v)

b = d[choice(list(d.keys()))]
# print(d[choice(list(d.keys()))])