def human_to_dog_years(human_years):
    if human_years < 0:
        return "Error: Please enter a non-negative number."

    if human_years <= 2:
        dog_years = 10.5 * human_years
    else:
        dog_years = 10.5 * 2 + 4 * (human_years - 2)

    return f"{human_years} human years is equal to {dog_years} dog years."

human_years = float(input("Enter the number of human years: "))
result = human_to_dog_years(human_years)
print(result)
