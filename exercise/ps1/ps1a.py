total_cost = float(input("The cost of your dream home: "))
annual_salary = float(input("The starting annual salary: "))
portion_saved = float(input("The portion of salary to be saved: "))
portion_down_payment = 0.25
interest = 0.04


def cal_num_of_months():
    current_savings = 0
    num_of_months=0
    while (current_savings<total_cost*portion_down_payment):
        current_savings+= ((annual_salary/12)*portion_saved)+(current_savings*interest/12)
        num_of_months += 1
    return num_of_months


print(cal_num_of_months())

