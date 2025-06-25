''' 
PROBLEM 04: Largest Palindrome Product

A palindromic number reads the same both ways. The largest palindrome made from the product of 
two-digit numbers is 91 x 99 = 9009.

Find the largest palindrome made from the product of three-digit numbers.
'''

# checks if number is palindrome or not
def is_palindrome(num: int) -> bool:
  num_str = str(num)
  rev_num_str = num_str[::-1]
  
  return num_str == rev_num_str


# to get the list of all the possible numbers from provided length
def get_possible_nums(length: int, **kwargs):
  
  start = 10 ** (length - 1)
  end = (10 ** length)
  
  if 'start' in kwargs:
    if kwargs['start'] > start:
      start = kwargs['start']
    
    else:
      raise ValueError(f'start should be greater than { start } and less than { end }')
  
  
  for _ in range(start, end):
    yield _
  
  # end: get_possible_nums



# returns the biggest palindrome number according to the length provided
def get_biggest_palindrome(len: int) -> int:
  ans = 0
  
  for num in get_possible_nums(len):
    # debug print
    # print(f'{ num }: { is_palindrome(num) }')
    
    if is_palindrome(num) and num > ans:
      ans = num
    
  return ans


def get_biggest_product_palindrome(len: int) -> dict:
  res: dict = {
    'op1': 0,
    'op2': 0,
    'result': 0,
  }
  
  for x in get_possible_nums(len):
    for y in get_possible_nums(len):
      prod = x * y
      
      if is_palindrome(prod) and res['result'] < prod:
        res['op1'] = x
        res['op2'] = y
        res['result'] = prod
  
  return res

# solution
def solution():
  print(f'largest palindrome of length 2-digit is { get_biggest_palindrome(2) }')
  print(f'largest palindrome of length 3-digit is { get_biggest_palindrome(3) }')
  
  
  # printer func
  def printer(len: int, op1: int, op2: int, res: int):
    return f'largest product of {len} digit palindrome is: {op1} x {op2} = {res}'
    
  
  two_digit = get_biggest_product_palindrome(2)
  three_digit = get_biggest_product_palindrome(3)
  
  
  print(printer(2, two_digit['op1'], two_digit['op2'], two_digit['result']))
  print(printer(3, three_digit['op1'], three_digit['op2'], three_digit['result']))

solution()

