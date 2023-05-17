# Net Salary Calculator
total_salary = int(input("Enter your total salary: "))
tax_percent = int(input("Enter your salary tax rate as a number: "))
tax_conversion = tax_percent / 100
net_salary = print("Your net salary is:", total_salary - (total_salary * tax_conversion))
