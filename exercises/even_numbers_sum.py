import random;

def generate_int_array():
    return [random.randint(0, 100) for _ in range(10)];

def is_even(number):
    return number % 2 == 0;

def sum_even_numbers(array):
    return sum([number for number in array if is_even(number)]);

def main():
    array = generate_int_array();
    result = sum_even_numbers(array);
    print(f"Generated array: {array}");
    print(f"Sum of its even numbers: {result}");

main();