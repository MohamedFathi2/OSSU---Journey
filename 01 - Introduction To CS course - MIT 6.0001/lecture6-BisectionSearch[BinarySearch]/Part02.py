'''
Write code to do bisection search to find the cube root of positive cubes within 
some epsilon. Starting with the following parameters
'''
cube = 27
epsilon = 0.01
low = 0
high = cube
guess = (low + high) / 2
num_guesses = 0
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (low + high) / 2
    num_guesses += 1


print(f"Number of guesses = {num_guesses}")
print(f"{guess} is close to cube root of {cube}")
