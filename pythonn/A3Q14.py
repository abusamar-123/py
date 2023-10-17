def is_palindrome(number):
    number_str = str(number)
    return number_str == number_str[len(number_str)::-1]
num = int(input("Enter a number: "))   
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
