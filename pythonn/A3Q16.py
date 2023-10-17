def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    digit_sum = sum(int(digit) ** num_digits for digit in num_str)
    return number == digit_sum

for num in range(1, 1001):
    if is_armstrong_number(num):
        print(num)
