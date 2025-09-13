def tupple_product(numbers):
    product = 1
    for num in numbers :
        product *=num
    return product

my_tuple = (2,3,4,5)

result = tupple_product(my_tuple)

print("Tuple:", my_tuple)
print("Product of all numbers:", result)