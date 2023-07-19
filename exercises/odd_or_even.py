def run_prompt():
    return float(input('Enter number to be analyzed: '));

def is_even(number):
    return number % 2 == 0;

def result_message(result):
    return f"This number is {result}";

def main():
    number = run_prompt();
    result = 'even' if is_even(number) else 'odd';
    print(result_message(result));

main();
    