'''
Finger exercise: Write a program that prints the sum of the prime
numbers greater than 2 and less than 1000. Hint: you probably want
to use a for loop that is a primality test nested inside a for loop that
iterates over the odd integers between 3 and 999.
'''
sum = 0
flag = True # flag to indicate that it is a prime number.
for num in range(3, 999):
    if num % 2 != 0:
        flag = True # Reset flag for each new number
        for testing in range(3, num, 2):
            if num % testing == 0:
                flag = False
                break
        if flag:
            sum += num
print(f"sum of prime numbers in range 3 to 999 is: {sum}")


# Another Implementation:
'''
sum = 0
for num in range(3, 999):
    if num % 2 != 0:
        for testing in range(3, num, 2):
            if num % testing == 0:
                flag = False
                break
        else: # for-else structure can help here. The else block executes only if the loop did not break,
              #which means the number is prime
            sum += num
print(f"sum of prime numbers in range 3 to 999 is: {sum}")
'''