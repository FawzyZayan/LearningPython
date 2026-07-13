import time

def calculate_tax(income):
  return income * 0.15

def calculate_total_salary(base_salary, bonus):
  total_salary = base_salary + bonus
  tax_to_pay = calculate_tax(total_salary)
  return total_salary - tax_to_pay
  

base_salary = float(input("Enter your base salary: "))
bonus = float(input("Enter the bonus you got: "))

final_salary = calculate_total_salary(base_salary, bonus)


time.sleep(3)
print("Calculating your Total Salary... Please Wait")
time.sleep(2)
print("Calculating the Tax Amount... Please Wait")
time.sleep(2)
print("Calculating the Final Salary... Please Wait")
time.sleep(2)
print(f"Final Salary after tax is: ⃁{final_salary}")