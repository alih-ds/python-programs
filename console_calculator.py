# Arithmetic Calculator
print("First number:")
first_number = float(input())
print()
print("Operator:")
operation = str(input())
print()
print("Second number:")
second_number = float(input())
print()
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
print("Result:")
print(result)