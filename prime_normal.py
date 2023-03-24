import math


def is_prime(m):
  if m < 2:
    return False
  for i in range(2, int(math.sqrt(m))+1):
    if m % i == 0:
      return False
  return True
  
  
def prime_normal(n):
  c = []
  for i in range(n):
    if is_prime(i):
      c.append(i)
  return c
              
