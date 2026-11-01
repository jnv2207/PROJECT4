
# Project: Data Analyzer and Transformer

# Global Variables
data = []
dataset_summary = {}


# A. Built-in Functions
def display_summary():
    """Display basic statistics using built-in functions."""

    global dataset_summary

    values = flatten_data(data)

    if not values:
        print("Please enter data first.")
        return

    total = len(values)
    minimum = min(values)
    maximum = max(values)
    total_sum = sum(values)
    average = total_sum / total

    dataset_summary = {
        "Total Elements": total,
        "Minimum": minimum,
        "Maximum": maximum,
        "Sum": total_sum,
        "Average": round(average, 2)
    }

    print("\n--- DATA SUMMARY ---")
    for key, value in dataset_summary.items():
        print(key, ":", value)


# Helper Function
def flatten_data(dataset):
    """Convert 1D or 2D list into a single 1D list."""

    if not dataset:
        return []

    if isinstance(dataset[0], list):
        return [value for row in dataset for value in row]

    return dataset.copy()


# B. User Defined Functions
def calculate_average():
    """Calculate average of dataset."""

    values = flatten_data(data)

    if values:
        return sum(values) / len(values)

    print("No data available.")
    return None


def find_duplicates():
    """Find duplicate values in dataset."""

    values = flatten_data(data)
    duplicates = []

    for value in values:
        if values.count(value) > 1 and value not in duplicates:
            duplicates.append(value)

    print("Duplicate values:", duplicates if duplicates else "None")


def display_unique():
    """Display unique values in dataset."""

    values = flatten_data(data)
    unique = list(set(values))

    print("Unique values:", sorted(unique))


# C. *args and **kwargs
def show_values(*args):
    """Accept and display multiple values."""

    print("Values:", args)


def show_characteristics(**kwargs):
    """Display dataset characteristics using keyword arguments."""

    print("\n--- DATASET CHARACTERISTICS ---")

    for key, value in kwargs.items():
        print(key, ":", value)


# D. Recursion
def factorial(n):
    """Calculate factorial using recursion."""

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


# E. Lambda Function
def filter_data():
    """Filter values using lambda and filter function."""

    values = flatten_data(data)

    if not values:
        print("Please enter data first.")
        return

    try:
        threshold = float(input("Enter threshold value: "))

        above = list(filter(lambda x: x > threshold, values))
        below = list(filter(lambda x: x < threshold, values))

        doubled = list(map(lambda x: x * 2, values))

        print("Values above threshold:", above)
        print("Values below threshold:", below)
        print("Doubled values:", doubled)

    except ValueError:
        print("Please enter a valid number.")


# F. Global Keyword
def update_global_summary():
    """Update global dataset summary."""

    global dataset_summary

    values = flatten_data(data)

    if values:
        dataset_summary = {
            "Total": len(values),
            "Mean": sum(values) / len(values)
        }

        print("Global summary updated:", dataset_summary)
    else:
        print("Please enter data first.")


# G. Return Multiple Values
def get_statistics():
    """Return minimum, maximum and average."""

    values = flatten_data(data)

    if not values:
        return None, None, None

    minimum = min(values)
    maximum = max(values)
    average = sum(values) / len(values)

    return minimum, maximum, average


def display_statistics():
    """Display multiple returned statistics."""

    minimum, maximum, average = get_statistics()

    if minimum is None:
        print("Please enter data first.")
    else:
        print("Minimum:", minimum)
        print("Maximum:", maximum)
        print("Average:", round(average, 2))


# H. 1D and 2D Lists
def input_data():
    """Accept 1D or 2D list from user."""

    global data

    print("\n1. Enter 1D List")
    print("2. Enter 2D List")
    print("3. Use Sample 1D Data")
    print("4. Use Sample 2D Data")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            data = list(map(float, input(
                "Enter values separated by spaces: "
            ).split()))

        elif choice == 2:
            rows = int(input("Enter number of rows: "))
            data = []

            for i in range(rows):
                row = list(map(float, input(
                    f"Enter values for row {i + 1}: "
                ).split()))
                data.append(row)

        elif choice == 3:
            data = [34, 12, 56, 78, 43, 21, 90]

        elif choice == 4:
            data = [
                [10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]
            ]

        else:
            print("Invalid choice.")
            return

        print("Data stored successfully!")
        display_data()

    except ValueError:
        print("Invalid input. Please enter numbers only.")


def display_data():
    """Display data in list or grid format."""

    if not data:
        print("No data available.")
        return

    print("\n--- DATASET ---")

    if isinstance(data[0], list):
        for row in data:
            print(" | ".join(map(str, row)))
    else:
        print(data)


# I. Sorting Collection Data Types
def sort_data():
    """Sort 1D and 2D lists."""

    if not data:
        print("Please enter data first.")
        return

    try:
        print("\n1. Ascending Order")
        print("2. Descending Order")

        choice = int(input("Enter choice: "))

        if isinstance(data[0], list):
            result = [sorted(row, reverse=(choice == 2))
                      for row in data]

            print("Sorted 2D List:", result)

        else:
            if choice == 1:
                data.sort()
            elif choice == 2:
                data.sort(reverse=True)
            else:
                print("Invalid choice.")
                return

            print("Sorted Data:", data)

    except ValueError:
        print("Enter a valid choice.")


# Main Menu
def main():

    print("\nWELCOME TO DATA ANALYZER AND TRANSFORMER")

    while True:

        print("\n========== MAIN MENU ==========")
        print("1. Input Data")
        print("2. Display Data Summary")
        print("3. Calculate Factorial (Recursion)")
        print("4. Filter Data (Lambda Function)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics")
        print("7. Find Average")
        print("8. Find Duplicate Values")
        print("9. Display Unique Values")
        print("10. Demonstrate *args and **kwargs")
        print("11. Update Global Summary")
        print("12. Display Data")
        print("13. Display Function Documentation")
        print("14. Exit Program")

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                input_data()

            elif choice == 2:
                display_summary()

            elif choice == 3:
                try:
                    number = int(input("Enter a number (0-100): "))

                    if 0 <= number <= 100:
                        print("Factorial:", factorial(number))
                    else:
                        print("Enter a number between 0 and 100.")

                except ValueError:
                    print("Enter a valid integer.")

            elif choice == 4:
                filter_data()

            elif choice == 5:
                sort_data()

            elif choice == 6:
                display_statistics()

            elif choice == 7:
                result = calculate_average()

                if result is not None:
                    print("Average:", round(result, 2))

            elif choice == 8:
                find_duplicates()

            elif choice == 9:
                display_unique()

            elif choice == 10:
                values = flatten_data(data)

                show_values(*values)

                show_characteristics(
                    Total=len(values),
                    Sum=sum(values) if values else 0,
                    Minimum=min(values) if values else "N/A",
                    Maximum=max(values) if values else "N/A"
                )

            elif choice == 11:
                update_global_summary()

            elif choice == 12:
                display_data()

            elif choice == 13:
                print("\nFUNCTION DOCUMENTATION")
                print(display_summary.__doc__)
                print(calculate_average.__doc__)
                print(factorial.__doc__)
                print(filter_data.__doc__)
                print(sort_data.__doc__)

            elif choice == 14:
                print("Thank you for using Data Analyzer!")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Please enter a valid menu number.")


# Program Execution
if __name__ == "__main__":
    main()
