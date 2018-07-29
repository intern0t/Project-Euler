# https://projecteuler.net/problem=4

import time

lowerLimit = 900 # Because, according to the question, 2 digit highest is close to 90+ (91*99=9009)
upperLimit = 1000
palindromes = []

def productPrinter(p1, p2):
    theProduct = p1 * p2
    if str(theProduct) == str(theProduct)[::-1]:
        palindromes.append([p1, p2])
        print("[%d*%d] = %s => %s" % (p1, p2, str(theProduct), "Palindrome"))
        time.sleep(.1)
    else:
        print("[%d*%d] = %s => %s" % (p1, p2, str(theProduct), "Not Palindrome"))
    if p2 < upperLimit:
        productPrinter(p1, p2+1)

while lowerLimit < upperLimit:
    productPrinter(lowerLimit, lowerLimit)
    lowerLimit += 1

largest = palindromes[0][0] * palindromes[0][1]
combo = []
for productCombo in palindromes:
    temp = productCombo[0] * productCombo[1]
    if temp > largest:
        largest = temp
        combo = productCombo

print(palindromes)
print("Largest product palindrome in [%d,%d] is %d." % (combo[0], combo[1], largest))
