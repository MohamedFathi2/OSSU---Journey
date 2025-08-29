#x = int(input("What x to find the cube root of? "))
#g = int(input("What guess to start with? "))
#print('Current estimate cubed = ', g**3)

#next_g = g - ((g**3 - x) / (3*g**2))
#print("Next guess to try = ", next_g)


# if conditionals
#pset_time = 20
#sleep_time = 4
#if((pset_time + sleep_time) > 24):
#    print("Impossible!")
#elif (pset_time + sleep_time) == 24:
#    print("full schedule!")
#else:
#    leftover = abs(24 - pset_time - sleep_time)
#    print(leftover, "h of free time!")
#print("end of day")


# write a program that:
# saves a secret number
# asks the user for a number guess
# prints whether the guess is too low, too high, or the same as the secret

secret = 101
guess = int(input("Take a guess: "))

if (secret == guess):
    print("Congrats! you guessed correctly!")
elif (guess > secret):
    print("Guess is too high")
else:
    print("Guess is too low")
print("Thanks for playing!")
