numbers = [0,1,1,2,3,5,8,13,21,34]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers))