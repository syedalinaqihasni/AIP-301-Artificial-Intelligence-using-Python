salary = float(input("Enter your salary: "))

if salary < 30000:
    tax_rate = 0.05
elif 30000 <= salary <= 70000:
    tax_rate = 0.15
else:
    tax_rate = 0.25

tax = salary * tax_rate
final_salary = salary - tax

print("Tax Rate:", tax_rate * 100, "%")
print("Tax Amount:", tax)
print("Final Salary after tax:", final_salary)