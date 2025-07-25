'''
PROBLEM 02:

Each new term in the Fibonacci sequence is generated by adding the previous 
two terms. By starting with 1 and 2, the first terms will be:

By considering the terms in the Fibonacci sequence whose values do not exceed 
four million, find the sum of the even-valued terms.
'''


def fibonacci_at(pos):
  if pos <= 0:
    return 1
  
  if pos <= 2:
    # print('broke')
    return pos
  
  return fibonacci_at(pos - 1) + fibonacci_at(pos - 2)


def fibonacci_seq(count, **kwargs):
  start = kwargs.get('start', 0)
  end = count + start
  
  for i in range(start, end):
    print(fibonacci_at(i))

# Checks if number is even or not
def is_even(n: int | float):
  return n % 2 == 0

# Generates the fibonacci sequence
def fibonacci_gen(count, **kwargs):
  start = kwargs.get('start', 0)
  end = count + start
  
  for i in range(start, end):
    yield fibonacci_at(i)


# Main
def main():
  sum = 0
  
  for i in fibonacci_gen(10):
    print(i)
  
  if is_even(i):
    sum = sum + i
    
  print("\nSum = " + str(sum))

