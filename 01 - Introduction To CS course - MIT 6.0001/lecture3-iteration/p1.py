'''
counter = 0
where = input("You're in the lost Forest. Go left or right? ")
while (where == 'right'):
    counter += 1
    if counter > 2:
        print(":(")
    where = input("You're in the lost Forest. Go left or right? ")
print("You got out of the lost Forest!")
'''
'''
x = 4
i = 1
fact = 1
while i <= x:
    fact *= i
    i += 1
print(f'{x} factorial is {fact}')
'''
mysum = 0
start = 3
end = 5
for i in range(start, end + 1):
    mysum += i
print(mysum)