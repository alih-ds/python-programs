# Arithmetic Calculator
first_number = float(input("First number: "))
operation = str(input("Operator: "))
second_number = float(input("Second number: "))
if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "*":
    result = first_number * second_number
elif operation == "/":
    result = first_number / second_number
elif operation == "**":
    result = first_number ** second_number
else:
    print("Error")
print("Result:", result)