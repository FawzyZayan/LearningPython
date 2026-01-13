base_salary = float(input("Enter your base salary: "))
bonus = float(input("How much bonus did you get: "))


money = base_salary + bonus

money_after_tax = money - 0.15 * money

print(f"Your final salary after tax: ${money_after_tax} ")