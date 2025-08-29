x = 54321
epsilon = 0.01
num_guesses = 0
low =  0
high = x
guess = (low + high) / 2.0
while abs(guess**2 - x) >= epsilon:
    if guess**2 < x:
        low = guess
    elif guess**2 > x:
        high = guess
    guess = (low + high) / 2.0
    num_guesses += 1
    
print(f"Number of guesses = {num_guesses}")
print(f"{guess} is close to square root of {x}")
