# https://projecteuler.net/problem=2

def nextFibonacci(preTwo):
    toReturn = preTwo
    newNumber = preTwo[-1] + preTwo[-2]
    toReturn.append(newNumber)
    return toReturn

startOff = nextFibonacci([1, 2])

while (startOff[-1] < 4000000):
    startOff = nextFibonacci(startOff)
    print(startOff)

totalSum = 0
for i in startOff:
    if i % 2 == 0:
        totalSum += i
print("\n%d\n" % totalSum)
