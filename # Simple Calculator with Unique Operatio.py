# Simple Calculator with Unique Operation Selector

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

def select_operation():
    operations = {
        '1': ('Addition', lambda x, y: x + y),
        '2': ('Subtraction', lambda x, y: x - y),
        '3': ('Multiplication', lambda x, y: x * y),
        '4': ('Division', lambda x, y: x / y if y != 0 else 'Undefined (division by zero)')
    }

    print("\nSelect an operation:")
    for key, (name, _) in operations.items():
        print(f"{key}. {name}")

    while True:
        choice = input("Enter the operation number: ")
        if choice in operations:
            return operations[choice]
        else:
            print("Invalid selection! Please choose a valid operation.")

def perform_calculation():
    print("Welcome to the Simple Calculator!\n")
    
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")

    operation_name, operation_func = select_operation()
    result = operation_func(num1, num2)

    print(f"\nResult of {operation_name}: {result}")

if __name__ == "__main__":
    perform_calculation()
