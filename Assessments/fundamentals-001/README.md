# Project Description
In this assessment, you will create a Python program that performs various data transformations and analyses on sequences. The project focuses on string manipulation, mathematical operations, and pattern recognition, reinforcing your understanding of unit testing, loops, conditionals, and algorithmic thinking.

## Module Structure


```
fun-001-str-seq/
├── string_ops.py          # String operation functions
├── sequences.py           # Sequence generation functions
├── test_assessment.py     # Test cases for all functions (YOUR tests go here)
└── tests/
    └── test_my_tests.py   # Tests for test cases(DO NOT TOUCH TESTS-- Make these tests pass)
```


### Test-Driven Development (TDD) Requirements

Create the following file `test_assessment.py`.

For this assessment, you must follow Test-Driven Development (TDD) principles:

- Write test cases before implementing functions.
- Ensure tests cover both normal operations and edge cases.
- Use the tests to guide your function implementations.
- Note: In addition to the provided test cases, hidden tests will be run to verify the correctness of your implementation. These hidden tests will check edge cases and ensure your functions behave exactly as specified in the requirements.

Your test file should:

- Use Python's unittest framework.
- Name the test class `MyTestClass`.
- Include separate test methods for each function and any tests you deem necessary. 

---

### String Operations

`string_ops.py`.

Create this file with the following functionality:

- A function to count vowels in a string: `count_vowels(text: str) -> int`

    - Example: `count_vowels("Zakumi") -> 3`

- A function that reverses each word in a sentence: `reverse_each_word(sentence:str) -> str`

    - Example: `reverse_each_word("hello world") -> "olleh dlrow"`

---

### Sequences

`sequences.py`

Create this file with the following functionality:

- A function that generates factorials: `generate_factorial_series(n: int) -> list`
    - `generate_factorial_series(4) -> [1, 2, 6, 24]`

- A function that generates the first `n` multiples of a multiplier: `generate_multiples(n: int, multiplier: int) -> list`

    - Example: `generate_multiples(5, 3) -> [3, 6, 9, 12, 15]`

---

### Definitionstest

- **Palindrome**: A string that reads the same backward as forward. Example: `"radar", "level", "madam"`

- **Vowels**: In English, vowels are the letters `a, e, i, o, u`

- **Multiples**: A multiple of a number is the product of that number and any integer. In other words, if you multiply a number by an integer, the result is a multiple of the original number. 

    Examples:

    Multiples of 3: `3, 6, 9, 12, 15, 18, 21, 24, ...`

    Multiples of 5: `5, 10, 15, 20, 25, 30, 35, ...`

- **Factorial**: The factorial of a non-negative integer n, denoted as n!, is the product of all positive integers less than or equal to n. 

Examples:

```
- 0! = 1 (by definition)
- 1! = 1
- 2! = 2 × 1 = 2
- 3! = 3 × 2 × 1 = 6
- 4! = 4 × 3 × 2 × 1 = 24
- 5! = 5 × 4 × 3 × 2 × 1 = 120
```

## Overview Module Structure

assessment_project/
├── string_ops.py          # String operation functions
├── sequences.py           # Sequence generation functions
├── test_assessment.py     # Test cases for all functions (YOUR tests go here)
└── tests/
    └── test_my_tests.py   # Tests for test cases(DO NOT TOUCH TESTS-- Make these tests pass)