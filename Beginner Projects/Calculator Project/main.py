import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

should_accumulate = True
first_number = int(input("Enter the first number: "))

while should_accumulate:

    for operator in operations:
        print(operator)

    operator = input("Pick an operator: ")
    second_number = int(input("Enter the second number: "))

    answer = operations[operator](first_number, second_number)

    print(f"Answer: {first_number} {operator} {second_number} = {answer}")

    next_decision = input(
        "You want to continue working with the result? Yes or No? "
    ).lower()

    if next_decision == "yes":
        first_number = answer
    else:
        should_accumulate = False