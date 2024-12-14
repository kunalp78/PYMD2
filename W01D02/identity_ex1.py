"""
This file shows the example for "is" identity operator
"""
# identity operator

a = 23
b = 23

# print(id(a), id(b))
# print(a is b)

# a = 24
# b = 23
# print(id(a), id(b))
# print(a is b)
# x = (1, 2, 3)
# y = (1, 2, 3)
# print(x is y)
# print(id(x), id(y))


a1 = [1, 2, 3]
a2 = [1, 2, 3]
print(a1 == a2)
print(a1 is a2)
print(id(a1), id(a2))