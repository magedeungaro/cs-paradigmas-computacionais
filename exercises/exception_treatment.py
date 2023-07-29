def run_prompt():
    return input('Enter a number: ');

def is_valid_input(value):
    try:
        float(value);
        return True;
    except (TypeError, ValueError):
        return False;

def main():
    number = run_prompt();
    while not is_valid_input(number):
        print('Not a valid number. Try again.');
        number = run_prompt();
    print(number);

main();

