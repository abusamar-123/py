def calculate_series(x, n):
    result = 0
    sign = 1

    for i in range(1, n + 1):
        term = (-1) ** (i - 1) * (x ** (2 * i - 1)) / factorial(2 * i - 1)
        result += sign * term
        sign *= -1

    return result

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms (n): "))

if n < 0:
    print("Number of terms (n) must be non-negative.")
else:
    result = calculate_series(x, n)
    print(f"The result of the series is approximately: {result:.4f}")
