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
'''
You have just graduated from MIT and have a job! You move to the Bay Area and decide that you want to start saving for a home. Houses are fairly
expensive, so you start saving up for the down payment on your dream home.

Your goal is to find the number of months it takes to save up for a down payment. The cost of your down payment is calculated by 
# multiplying the total cost of your dream house by the down payment percentage.
totalcost * downpaymentPercentage
User Inputs. Ask the user to enter the following variables and cast them as floats. They must be initialized in the following order at the beginning of
your program, before declaring other variables.
1. The starting yearly salary ( yearly_salary)
2. The portion of salary to be saved ( portion_saved). This variable should be in decimal form (e.g. 0.1 for 10%).
3. The cost of your dream home ( cost_of_dream_home)
Writing the Program. You will need to determine how many months it will take given the following information:
1. yearly_salary, as described above.
2. portion_saved, as described above.
3. cost_of_dream_home, as described above.
4. portion_down_payment, the percentage of the total cost needed for a down payment. Assume portion_down_payment = 0.25 (25%).
5. The amount that you have saved thus far is amount_saved, which starts at $0.
6. You get an annual rate of return r. In other words, at the end of each month, you receive an additional amount_saved * (r/12) funds for your
savings (the 12 is because r is an annual rate). Assume r = 0.05 (5%).
7. At the end of each month, your savings increase by (1) a percentage of your monthly salary and (2) the monthly return on your investment. (Note:
The investment amount used to calculate the monthly return is the amount you had saved at the start of each month.)
Output.
1. Your program should store the number of months required to save for the down payment using a variable called months.

'''
yearly_salary = float(input("Enter your yearly salary: "))
monthly_salary = yearly_salary / 12.0
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ")) # this should be in decimal form - eg: 0.1 for 10%
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
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


print(f"Number of months: {months}")