# Check if a number is prime or not
num = int(input("Please enter a number: "))
if num <= 1:
    print(num, "is not a prime number.")
elif num == 2:
    print(num, "is a prime number.")
elif num % 2 == 0 and num % num == 0:
    print(num, "is not a prime number.")
else:
    print(num, "is a prime number.")