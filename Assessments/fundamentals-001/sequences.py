"""
### Sequences

`sequences.py`

Create this file with the following functionality:

- A function that generates factorials: `generate_factorial_series(n: int) -> list`
    - `generate_factorial_series(4) -> [1, 2, 6, 24]`

- A function that generates the first `n` multiples of a multiplier: `generate_multiples(n: int, multiplier: int) -> list`

    - Example: `generate_multiples(5, 3) -> [3, 6, 9, 12, 15]`

---"""

def factorial(num):

  k = 1
  for n in range(num):
    k *= (n+1)
  
  return k



def generate_factorial_series(n: int) -> list:

  if n == 0:
    return [0]
  
  return [factorial(num + 1) for num in range(n)]


def generate_multiples(n: int, multiplier: int) -> list:

  return [multiplier * (num + 1) for num in range(n)]




