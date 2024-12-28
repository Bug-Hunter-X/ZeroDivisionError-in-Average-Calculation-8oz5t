def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

#Improved version using exception handling
def calculate_average_improved(numbers):
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        return 0    except TypeError:
        return "Invalid input"