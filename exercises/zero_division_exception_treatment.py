def run_prompt(message):
    number = input(message);
    while not is_valid_input(number):
        print('Not a valid number. Try again.');
        number = input(message);
    return float(number);

def is_valid_input(value):
    try:
        float(value);
        return True;
    except (TypeError, ValueError):
        return False;

def divide(dividend, divisor):
    try:
        result = dividend / divisor;
        return "{:.2f}".format(result);
    except ZeroDivisionError:
        return 'It is not possible to divide by zero';

def main():
    dividend = run_prompt('Enter dividend: ');
    divisor = run_prompt('Enter divisor: ');
    print(f'Division operation: {dividend:.2f}/{divisor:.2f}');
    print(f'Result: {divide(dividend, divisor)}');

main();

