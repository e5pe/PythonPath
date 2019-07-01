
"""
table
object reference count
"""
a = "alc"
b = "alc"
# count increases in every reference to an object

a = 123 # now a is a number

print(a)
print(b)

c = "alc"
d = c
print(c == d)
print(d is c)