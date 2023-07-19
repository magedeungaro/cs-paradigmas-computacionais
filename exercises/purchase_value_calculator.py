def product_price():
    return 10.0;

def discount_quantity_thresholds():
    return { 'min': 10, 'max': 20 };

def discount_table():
    return { 'no_tier': 0.0, 'tier_1': 0.1, 'tier_2': 0.2 };

def get_discount(product_quantity, thresholds, discount_table):
    min_threshold = thresholds['min'];
    max_threshold = thresholds['max'];

    if product_quantity < min_threshold:
        return discount_table['no_tier'];

    return discount_table['tier_2'] if product_quantity > max_threshold else discount_table['tier_1'];

def calculate_purchase_value(product_price, product_quantity, discount):
    return product_price * product_quantity * (1 - discount);

def run_prompt():
    return int(input('How much do you want to buy? '));

def main():
    product_quantity = run_prompt();
    discount = get_discount(product_quantity, discount_quantity_thresholds(), discount_table());
    purchase_value = calculate_purchase_value(product_price(), product_quantity, discount);
    print(f"Your purchase value is: R$ {purchase_value:.2f}");

main();