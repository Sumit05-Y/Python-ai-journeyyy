#Print bool() of: 0, 1, -1, '', 'hello', [], None, 0.0, 3.14, ' ' (just a space).
# Write a comment explaining WHY each is truthy or falsy. The space one will surprise you

a=0     #   0 is a falsy value as it refers to no or LOW
b=1     #   1 is a truthy value as it refers to yes or HIGH
c=-1    #  -1 is a truthy value as it refers to yes or HIGH
d=''    #   '' is a falst value as it is a empty or denotes no or LOW
e='hello'#  'hello' is a truthy value as it has something written in it which is considered to be HIGH
f=None  #   None is a falsy value as it refers to LOW
g=0.0   #   0.0 is falsy as it refers to no or LOW
h=3.14  #   3.14 is a truthy value are it refers to yes or HIGH
i= ' '  #   ' ' is a truthy value as there is space for any of the value which will denotes as true or HIGH
for i in [a, b, c, d, e, f, g, h, i]:
    print(f"The boolean value is {bool(i)}")

