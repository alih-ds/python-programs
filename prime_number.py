# Check if a number is prime or not
num = int(input("Please enter a number: "))
if num <= 1:
    print(num, "is not a prime number.")
for i in range(2, num):
    if num % i == 0:
        print(num, "is not a prime number.")
        break
else:
    print(num, "is a prime number.")