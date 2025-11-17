def categorizeByAge(age):
    if age <= 0:
        return "Invalid age"
    elif age <= 9:
        return "Child"
    elif age <= 18:
        return "Teenager"
    elif age <= 65:
        return "Adult"
    elif age <= 120:
        return "Senior"
    else:
        return f"Invalid age: {age}"