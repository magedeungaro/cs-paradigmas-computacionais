import math;

def second_degree_function(a: int, b: int, c: int):
    # ax^2 + bx + c

    def calculate_delta(a, b, c):
        return b ** 2 - 4 * a * c;

    def calculate_roots(a, b, delta):
        if delta < 0:
            return None, None;

        if delta == 0:
            return -b / (2 * a), None;
        else:
            delta_sqrt = math.sqrt(delta);
            x1 = (-b + delta_sqrt) / (2 * a);
            x2 = (-b - delta_sqrt) / (2 * a);
            return x1, x2;

    delta = calculate_delta(a, b, c);
    return calculate_roots(a, b, delta);

def run_prompt():
    a = int(input('Enter a: '));
    b = int(input('Enter b: '));
    c = int(input('Enter c: '));

    return a, b, c;

def main():
    a, b, c = run_prompt();
    print(f"{a}x^2 + {b}x + {c}");
    print(f"real number roots = {second_degree_function(a, b, c)}");

main();

