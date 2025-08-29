'''Write a program that asks the user to input 10
integers, and then prints the largest odd number that was entered. If
no odd number was entered, it should print a message to that effect.'''
print("Enter 10 integers: ")
counter = 0
maxOdd = 0

while counter < 10:
    x = int(input(f"{counter + 1} integer: "))
    if x % 2 != 0 and x > maxOdd:
        maxOdd = x
    counter += 1
if (maxOdd == 0):
    print("No Odd numbers were entered.")
else:
    print(f"Largest Odd Number is: {maxOdd}")
