'''
PROBLEM 06: Sum Square Difference

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385.

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025.

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def sum_of_squares(end: int) -> int:
  sum = 0
  
  for x in range(end + 1):
    sum += x ** 2
  
  return sum

def square_of_sum(end: int) -> int:
  sum = 0
  
  for x in range(end + 1):
    sum += x
  
  return sum ** 2

def solution(end: int, start = 1):
  x = sum_of_squares(end)
  y = square_of_sum(end)
  
  diff = y - x
  
  print(f'From {start} to {end}:')
  print(f'\tsum of squares: {x}\n\tsquare of sum: {y}\n\tdifference: {diff}\n')
  #end
  

solution(10)
solution(100)