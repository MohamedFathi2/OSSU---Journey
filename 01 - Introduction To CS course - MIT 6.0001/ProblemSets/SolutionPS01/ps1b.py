## 6.100A PSet 1: Part B
## Name:
## Time Spent:
## Collaborators:

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################


#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################


###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

## 6.100A PSet 1: Part A
## Name:
## Time Spent:
## Collaborators:

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################


#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################


###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

yearly_salary = float(input("Enter your yearly salary: "))
monthly_salary = yearly_salary / 12.0
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ")) # this should be in decimal form - eg: 0.1 for 10%
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
portion_down_payment = 0.25 * cost_of_dream_home
amount_saved = 0
r = 0.05
months = 0
# what we need to determine is how many months it will take given the following information:

# yearly_salary, as described above
# portion_saved, as described above
# cost_of_dream_home, as described above
# portion_down_payment, assume it is 25% of the total cost

# you get an annual rate of return r. In other words, at the end of each month, you receive an additional amount_saved * (r/12) funds for your savings (the 12 is because 
# r is an annual rate). Assume r = 0.05 (5%)

# At the end of each month, your savings increase by:
# 1) a percentage of your monthly salary
# 2) the monthly return on your investment
#  (Note: The investment amount used to calculate the monthly return is the amount you had saved at the start of each month.)

# Output: 1. Your program should store the number of months required to save for the down payment using a variable called months.

while (amount_saved < portion_down_payment):
    # balance = amount_saved
    # interest = amount_saved * (r / 12)
    # deposit = portion_saved * monthly_salary
    # amount_saved += interest + deposit
    amount_saved += amount_saved * (r / 12)
    amount_saved += portion_saved * monthly_salary
    months += 1
    if months % 6 == 1 and months != 1:
        yearly_salary += yearly_salary * semi_annual_raise
        monthly_salary = yearly_salary / 12
        
print(f"Number of months: {months}")