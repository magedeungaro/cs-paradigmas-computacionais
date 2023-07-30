from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_with_reduce = reduce(lambda x, y: x + y, numbers)

print(list(numbers))
print(f"Sum with reduce(): {sum_with_reduce}")
print(f"Sum with sum(): {sum(numbers)}")