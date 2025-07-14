'''
PROBLEM 05: Smallest Multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''


def test_condition():
  num = 2520
  
  for i in range(1, 21):
    print(f'{num} / {i} = { num % i}')
  
  #end

def solution():
  start = 2
  end = 22
  found = False
  
  num = end
  result = None
  
  
  while result is None:
    print(f'for number: { num } - ')
    
    for div in range(start, end, 2):
      remainder = num % div
      print(f'\ttesting for { num } % { div } = {remainder}')
      
      if remainder > 0:
        print(f'\tbreak')
        break
      
      if div == (end - 2):
        print('----found')
        result = num
    
    num += 1
  
  print(f'Answer is: { result}')


# test_condition()

solution()