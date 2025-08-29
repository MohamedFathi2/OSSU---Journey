x = 0.625
p = 0
# % 1 grabs the decimal part only
# ex: 1.1 % 1 is equal to 0.1
while (((2**p) * x) % 1 != 0): # while the calculated number is not a whole int (there is a decimal in it)
    print(f"Current Number: {(2**p) * x}")
    print("Remainder = " + str(((2**p) * x) - int((2**p) * x)))
    p += 1
print((2**p) * x)
num = int((2**p) * x) 
result = ''
if num == 0:
    result = '0'

# to get the binary representation of a +ve number:
while num > 0:
    result = str(num % 2) + result
    num = num//2

print(result)
for i in range(p - len(result)):
    result = '0' + result
result = result[0:-p] + "." + result[-p:]
print(f"The binary representation of the decimal {x} is {result}")
