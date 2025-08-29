def calc_amount_saved(initial_deposit, r):
    return initial_deposit * (1 + (r/12))**36


# Fixed And Input
initial_deposit = float(input("Enter the initial deposit: "))
down_payment = 800000 * 0.25
steps = 0
high = 1.0
low = 0.0
epsilon = 100



if initial_deposit > down_payment - epsilon:
    r = 0.0    
    print(f"Best saving rate: {r}")
    print("Steps in bisection search: 0")


# checking to see if we made saved all of the return of investment [100%] for 3 years, would it be possible to
# pay the down_payment in the right difference [epsilon]? if not, don't continue cuz it wouldn't be possible. 
elif calc_amount_saved(initial_deposit, 1.0) < down_payment - epsilon: # if amount saved for 3 years at 100% is not enough, terminate.
    r = None
    print("Best saving rate: None")
    print("Steps in bisection search: 0")

else: 
    # we will use bisection search to calculate the least r to get the amount_saved to be equal to down_payment within acceptable margin.
    while True:
        steps += 1
        r = (high + low) / 2
        amount_saved = calc_amount_saved(initial_deposit, r)
        if amount_saved - down_payment >= epsilon: # if the amount saved is bigger than the down payment and bigger than acceptable margin, re-evaluate
            high = r # update high accordingly.
        elif down_payment - amount_saved >= epsilon: #  if the down_payment is bigger the amount saved and bigger than the acceptable margin, re-evaluate
            low = r # update low accordingly.
        else:
            print("Best savings rate: ", r)
            print("Steps in bisection search", steps)
            break