'''
PROBLEM 07: 10 001st Prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

from utils import is_prime
from typing import Generator

def generate_prime(limit: int) -> Generator[int, None, None]:
  count = 0
  num = 2
  
  while count < limit:
    
    if is_prime(num):
      count += 1
      yield num    
    
    num += 1
    # end: while
  
  # end: generate_prime


def solution():
  nth = 10001
  nth_prime = None
  
  for index, value in enumerate(generate_prime(nth)):
    # print(value)
    
    if nth == (index + 1):
      nth_prime = value
  
  # end: for
  
  print(f'{nth}-th prime is { nth_prime }')
  #end: solution      


solution()