import random;

def generate_int_array():
    return [random.randint(0, 100) for _ in range(10)];

def smallest_number(array):
    # without using min(array);
    min_num = array[0];

    for num in array:
        if num < min_num:
            min_num = num;
    
    return min_num;

def main():
    array = generate_int_array();
    result = smallest_number(array);
    print(f"Generated array: {array}");
    print(f"Smallest number: {result}");

main();