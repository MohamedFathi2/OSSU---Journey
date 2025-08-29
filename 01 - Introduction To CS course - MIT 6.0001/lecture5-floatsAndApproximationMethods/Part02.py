x = 54321
epsilon = 0.01
num_guesses = 0
guess = 0.0
increment = 0.00001

while abs(guess**2 - x) >= epsilon and guess**2 <= x:
    guess += increment
    num_guesses += 1
    if num_guesses % 100000 == 0:
        print(f"Current Guess = {guess}")
        print(f"Current Guess**2 - x  = {abs(guess**2 - x)}")
    #if num_guesses % 100000 == 0:
    #    input('continue?')
print(f"Number of guesses = {num_guesses}")
if abs(guess**2 - x) >= epsilon:
    # Exited cuz guess**2 > x
    print(f"Failed on square root of {x}")
else:
    # Exited cuz guess**2 is within epsilon
    print(f"{guess} is close to square root of {x}")