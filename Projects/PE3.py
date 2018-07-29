# https://projecteuler.net/problem=3

factors = [1]
toFactor = 600851475143

def primeFactor(toFactor):
    i = 2
    factors = []
    while i * i <= toFactor:
        if toFactor % i:
            i += 1
        else:
            toFactor //= i
            factors.append(i)
    if toFactor > 1:
        # Because, it is a multiplication of 1 and itself.
        factors.append(toFactor)
    return factors

factors = primeFactor(toFactor)
print(factors)
