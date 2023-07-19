def compare_two_numbers(number_one, number_two):
    def response(greater, lesser, equals = False):
        return  { 'greater': 'greater', 'lesser': lesser, 'equals': equals }

    if number_one == number_two:
        return response(number_one, number_two);

    return response(number_one, number_two) if number_one > number_two else response(number_two, number_one);

def result_message(result):
    if result['equals']:
        return "Both number are equal";

    return f"{result['greater']} is greater than {result['lesser']}";

def run_prompt():
    number_one = float(input('Enter first number: '));
    number_two = float(input('Enter second number: '));

    return number_one, number_two;

def main():
    number_one, number_two = run_prompt();
    result = compare_two_numbers(number_one, number_two);
    print(result_message(result));


main();
