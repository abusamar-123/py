def grade_obtained(marks):
    if 90 <= marks <= 100:
        return "A"
    elif 70 <= marks <= 89:
        return "B"
    elif 50 <= marks <= 69:
        return "C"
    elif 40 <= marks <= 49:
        return "D"
    elif 0 <= marks <= 39:
        return "F"
    else:
        return "Invalid input: Marks should be between 0 and 100."
marks = int(input("Enter the student's marks: "))
result = grade_obtained(marks)
print(f"The student's grade is: {result}")
