# https://projecteuler.net/problem=1

upperLimit = 1000
lowerLimit = 1
totalSum = 0
for i in range(lowerLimit, upperLimit):
	if i % 3 == 0 or i % 5 == 0:
		totalSum += (i)
print(totalSum)
