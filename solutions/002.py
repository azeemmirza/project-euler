def fibonacci(n):
  print(f'{n} +', end=' ')
  if n == 1:
    return 1
  
  return n + fibonacci(n - 1)
  


print(f'\n= {fibonacci(10)}')