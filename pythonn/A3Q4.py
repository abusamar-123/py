import random

result = random.randint(0, 36)

red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black_numbers = [i for i in range(1, 37) if i not in red_numbers]

if result == 0:
    print("The spin resulted in 0...")
    print("Pay 0")
elif result == 00:
    print("The spin resulted in 00...")
    print("Pay 00")
else:
    print(f"The spin resulted in {result}...")
    print(f"Pay {result}")

    if result in red_numbers:
        print("Pay Red")
    else:
        print("Pay Black")

    if result % 2 == 1:
        print("Pay Odd")
    elif result != 0:  
        print("Pay Even")

    if result >= 1 and result <= 18:
        print("Pay 1 to 18")
    elif result >= 19 and result <= 36:
        print("Pay 19 to 36")
