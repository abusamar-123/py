def sum_of_digits(number):
    num_str = str(number)
    digit_sum = 0
    for digit_char in num_str:
        if digit_char.isdigit():  
            digit = int(digit_char)  
            digit_sum += digit  
    return digit_sum
num = int(input("Enter a number: "))
result = sum_of_digits(num)
print(f"The sum of the digits in {num} is {result}.")
