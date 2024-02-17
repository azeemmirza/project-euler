# PROBLEM_03:
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
import math


# checks if provided divisor of num is true or not
def is_factor(n: int, divisor: int) -> bool:
    if (divisor == 0) or (n == 0):
        return False

    return n % divisor == 0


# checks if provided number is prime
def is_prime(n: int, div: int = None) -> bool:
    # Check if n=1 or n=0
    if n <= 1:
        return False

    # Check if n=2 or n=3
    if n == 2 or n == 3:
        return True

    # Check whether n is divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check from 5 to square root of n
    # Iterate i by (i+6)
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


primes = []
num: int = 600851475143

for x in range(num):
    if x == 0:
        continue

    print('checking for: ' + str(x))

    factored = is_factor(num, x)
    primed = is_prime(x)

    if primed and factored:
        print(str(x) + ' : ' + str(factored))
        primes.append(x)


print('\n\n ------------------\n')
print(primes)
