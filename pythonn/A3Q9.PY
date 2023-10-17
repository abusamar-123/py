def max_Number(a, b, c):
    def find_maximum(x, y):
        if x > y:
            return x
        else:
            return y

    max_ab = find_maximum(a, b)

    result = find_maximum(max_ab, c)
    
    return result
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number:"))
    
maximum = max_Number(num1, num2, num3)
    
print(f"The maximum isis {maximum}.")

