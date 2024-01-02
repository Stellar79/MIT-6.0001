interest = 0.04
down_payment = 0.25
semi_annual_raise = .07
total_cost = 1000000
# calculate total savings of 36 months
def cal_total_savings(portion_saved,annual_salary):

    month_salary = annual_salary/12
    total_savings = 0
    num_of_months = 36
    for i in range(num_of_months):
        num_of_months += 1
        total_savings+= (month_salary*portion_saved)+(total_savings*interest/12)
        if (num_of_months%6==0):
            month_salary+=month_salary*semi_annual_raise
    # print(portion_saved,total_savings)
    return total_savings



def find_savings_rate(annual_salary):
    high = 1
    low = 0 
    steps_in_bisection = 1
    epsilon = 100
    savings_rate=(high+low)/2 * 10000
    total_savings=cal_total_savings(savings_rate/10000,annual_salary)
    while (abs(total_savings-(total_cost*down_payment)))>=epsilon:
        if(total_savings>=total_cost*down_payment):
            high = savings_rate
        else:
            low = savings_rate
        savings_rate = int((high+low)/2)
        total_savings=cal_total_savings(savings_rate/10000,annual_salary)
        steps_in_bisection += 1
        
    return (savings_rate/10000,steps_in_bisection)

(saving_rate,steps_in_bisection) = find_savings_rate(10000)
print(saving_rate,steps_in_bisection)