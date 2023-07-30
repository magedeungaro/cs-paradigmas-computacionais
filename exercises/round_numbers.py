numbers = [9.56783, 7.57568, 3.00914, 6.2321]
precision = [2, 2, 3, 3]

zipped_list = list(zip(numbers, precision))

zipped_dict = map(lambda x: {'number': x[0], 'precision': x[1]}, zipped_list)

rounded_numbers = map(lambda x: round(x['number'], x['precision']), zipped_dict)
print(list(rounded_numbers))