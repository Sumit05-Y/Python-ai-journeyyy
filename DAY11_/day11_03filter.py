number=[1,2,3,4,5,6,7,8,9,10]
def even_number(x):
    if x % 2 == 0:
        return x
result = list(filter(even_number,number))
print(result)