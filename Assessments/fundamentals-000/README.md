# Assessment: Number Sequence Generator
## Project Description

In this assessment, you will create a Python program that works with various number sequences and checks for specific mathematical properties. This project will reinforce your understanding of unit testing, loops, conditionals, and basic mathematical algorithms.

## Test-Driven Development (TDD) Requirements

#### `test/test_assessment.py`

For this assessment, you must follow Test-Driven Development (TDD) principles:

- **Write test cases before implementing functions.**
- Ensure tests cover both normal operations and edge cases.
- Use the tests to guide your function implementations.
- **Note:** In addition to the provided test cases , hidden tests will be run to verify the correctness of your implementation. These hidden tests will check edge cases and ensure your functions behave exactly as specified in the requirements. Make sure your functions work correctly for all possible valid inputs, not just the test cases you've written.

Your test file should:

- Use Python's `unittest` framework.
- Name the test class **`MyTestClass`**.
- Include separate test methods for each function.
- Cover both valid inputs and edge cases (e.g., zero, negative numbers).

---


## Requirements

### Module Structure

#### `main.py`

This is the main file that runs the program. It imports and calls functions from the other modules.

- Ensure that `main.py` imports `prime_numbers.py` and `sequences.py`.
- Use this file to test and run your implemented functions.
- You may comment out function calls if a specific function is not yet implemented.

#### `prime_numbers.py`
Create this file with the following functionality:

- A function to check if a number is prime:  
  **`is_prime(num: int) -> bool`**  
- A function to generate prime numbers up to a limit:  
  **`generate_primes(limit: int) -> list`**  
  **NOTE:** Use `is_prime()` to determine if numbers are prime.  
- A function to find the sum of all primes up to a given limit:  
  **`sum_all_primes(limit: int) -> int`**  
  **NOTE:** Use `generate_primes()` to generate the list of primes.

#### `sequences.py`
Create this file with the following functionality:

- A function to generate the Fibonacci sequence:  
  **`generate_fibonacci(n: int) -> list`**
- A function to generate square numbers:  
  **`generate_squares(n: int) -> list`**
- A function to generate cube numbers:  
  **`generate_cubes(n: int) -> list`**
- A function to check if a number is in the Fibonacci sequence:  
  **`is_in_fibonacci_sequence(num: int) -> bool`**

---

## Mathematical Definitions

- **Fibonacci Sequence**: A sequence where each number is the sum of the two preceding ones, usually starting with `0` and `1`.  
  _Example:_ `0, 1, 1, 2, 3, 5, 8, 13, 21, ...`

- **Prime Number**: A natural number greater than `1` that is only divisible by `1` and itself.  
  _Example:_ `2, 3, 5, 7, 11, 13, ...`

- **Square Number**: The result of multiplying a number by itself.  
  _Example:_ `1, 4, 9, 16, 25, ...` (`1², 2², 3², 4², 5², ...`)

- **Cube Number**: The result of multiplying a number by itself three times.  
  _Example:_ `1, 8, 27, 64, 125, ...` (`1³, 2³, 3³, 4³, 5³, ...`)

