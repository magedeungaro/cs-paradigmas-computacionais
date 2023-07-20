def is_prime_iterative(number):
    if number <= 1:
        return False;

    limit = (number // 2) + 1;
    for i in range(2, limit):
        if number % i == 0:
            return False;
    return True;

def run_prompt():
    number = int(input('Enter an integer number: '));
    return number;

def result_message(is_prime):
    print_value = 'prime' if is_prime else 'not prime';
    return f"This number is {print_value}";

def main():
    number = run_prompt();
    result = is_prime_iterative(number);
    print(result_message(result));

main();

