def main():
    height, weight = run_prompt();
    imc = calculate_imc(height, weight);
    print(f"Seu imc é: {imc}");

def run_prompt():
    height = string_to_float(input("Digite sua altura em metros: "));
    weight = string_to_float(input("Digite seu peso em kg: "));
    return height, weight;

def calculate_imc(height, weight):
    return weight / (height ** 2);

def string_to_float(string):
    return float(string.replace(",", "."));


main();