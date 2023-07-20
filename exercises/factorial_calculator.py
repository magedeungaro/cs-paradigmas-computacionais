def calculate_factorial_recursive(number):
    if number == 0:
        return 1
    
    return number * calculate_factorial_recursive(number - 1);

def calculate_factorial_iterative(number):
    result = 1
    for num in range(1, number + 1):
        result *= num;

    return result;

def run_prompt():
    number = int(input('Enter an integer number: '));
    return number;

def result_message(calcutation_method, number):
    function = globals().get(f"calculate_factorial_{calcutation_method}");
    return f"Factorial result using {calcutation_method}: {function(number)}";

def main():
    number = run_prompt();
    print(result_message('recursive', number));
    print(result_message('iterative', number));

main();