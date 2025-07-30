'''
PROBLEM 10: Summation of Primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

# checks if num is prime.
# will only give you whole number, if divisible by itself or one.
def is_prime(num: int) -> bool:
  if num == 1 and num ==0:
    return False
  
  if num == 2:
    return True
  
  if num % 2 == 0:
    return False
  
  return 