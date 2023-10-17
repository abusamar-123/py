def days_in_month(month):
    month = month.lower()

    if month == "january" or month == "march" or month == "may" or month == "july" or month == "august" or month == "october" or month == "december":
        return "31 days"
    elif month == "april" or month == "june" or month == "september" or month == "november":
        return "30 days"
    elif month == "february":
        return "28 or 29 days (leap year)"
    else:
        return "Invalid month name"
month_name = input("Enter the name of the month: ")
result = days_in_month(month_name)
print(f"{month_name} has {result}.")
