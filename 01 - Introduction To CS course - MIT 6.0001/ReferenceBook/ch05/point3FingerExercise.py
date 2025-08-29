#Finger exercise: Write a list comprehension that generates all non-primes between 2 and 100.
nonPrimes = [x for x in range(4, 101) if any(x % y == 0 for y in range(2, x))]
print(nonPrimes)
