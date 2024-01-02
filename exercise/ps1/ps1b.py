portion_down_payment = 0.25
interest = 0.04


def cal_num_of_months(annual_salary, total_cost, portion_saved, semi_annual_raise):
    month_salary = annual_salary/12
    current_savings = 0
    num_of_months = 0
    while (current_savings<total_cost*portion_down_payment):
        num_of_months += 1
        current_savings+= (month_salary*portion_saved)+(current_savings*interest/12)
        if (num_of_months%6==0):
            month_salary+=month_salary*semi_annual_raise
    return num_of_months

total_cost = float(input("The cost of your dream home: "))
annual_salary = float(input("The starting annual salary: "))
portion_saved = float(input("The portion of salary to be saved: "))
semi_annual_raise = float(input("The semi annual salary raise: "))

print(cal_num_of_months(total_cost, annual_salary, portion_saved, semi_annual_raise))

