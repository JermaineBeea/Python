# Java Fundamentals Consolidation

In this assessment, you are required to implement a set of Java functions that demonstrate your understanding of key programming concepts.

The focus areas for this assessment include:

- Control flow (if/else, switch)
- Loops and recursion
- String and list manipulation
- Arithmetic operations
- Algorithmic thinking
- Test-driven development (TDD)
- Understanding of data structures

---

## 🧩 Project Structure

```
├── src/
│ └── main/
│ └── java/
│ └── wethinkco/
| └── de/  
│ └── Consolidation.java # Your implementation goes here
├── src/
│ └── test/
│ └── java/
│ └── wethinkcode/
| └── de/
│ └── ConsolidationTest.java # Your unit tests go here
└── README.md
```

## `ConsilidationTest.java`
For this assessment, you must follow Test-Driven Development (TDD) principles:

- Write test cases before/alongside implementing the functionilities.


To check if **your** code passes **your** own test cases, run:

```bash
mvn test
```

***NB: You can run(copy and paste) the following commands on your terminal to run our hidden tests against your implementation***

```bash
chmod +x .lms/run_hidden.sh  #Run this only once
```

```bash
.lms/run_hidden.sh   #You can run this every time you want to test against the hidden tests
```


## `Consilidation.java`

1. `fizzBuzz(int n): List<String>`


**Parameters**:
n — The number up to which the FizzBuzz sequence should be generated. Must be a positive integer.

**Returns**:
A List<String> containing n elements that represent the FizzBuzz output from 1 to n.

- If the number is divisible by both 3 and 5, add "FizzBuzz" to the list.

- If the number is divisible by only 3, add "Fizz" to the list.

- If the number is divisible by only 5, add "Buzz" to the list.

- If the number is not divisible by 3 or 5, add the number itself as a string.

e.g: `fizzBuzz(15)`
```java
["1", "2", "Fizz", "4", "Buzz",
  "Fizz", "7", "8", "Fizz", "Buzz",
  "11", "Fizz", "13", "14", "FizzBuzz"
]
```

---null

2. `fibonacciSequence(int n): String`

**Parameters**:
n — The number of Fibonacci numbers to generate. Must be a non-negative integer.

**Returns**:
A String representing the first n numbers in the Fibonacci sequence, separated by a single space.

The Fibonacci sequence starts from 0 and 1, and each subsequent number is the sum of the previous two.

If n == 0, return an empty string.
If n == 1, return "0".

e.g: ``fibonnaciSequence(7)``
```java
"0 1 1 2 3 5 8"
```

---

3. `calculate(int a, int b, String operator): String`

**Parameters**:
null
- a — The first integer operand.

- b — The second integer operand.

- operator — The arithmetic operation to apply. Supported values:

    ` "+", "-", "*", "/", "%"`

**Returns**:

A String representing the result of the arithmetic operation.

e.g:

```java
calculate(10, 3, "+")  // "13"
calculate(10, 3, "%")  // "1"
calculate(10, 3, "/")  // "3"
```
---

4. `drawTriangle(int n): String`git@gitlab.wethinkco.de:jebeeajhb024/jav-000-fun.git

A String representation of a left-aligned triangle made of asterisks (*), with one asterisk on the first row, two on the second, and so on.

e.g: ``drawTriangle(3)``
```java
"*
**
***"
```

---

5. `ìsPalindrome(String str): boolean`

**Parameters**:
string — The string to check.

**Returns**:
true if the string reads the same forwards and backwards, false otherwise.

Palindrome comparison should be case-sensitive.

Ignore punctuation — "madam" is valid, "Madam" is valid.

e.g 
```java
isPalindrome("racecar")     // true
isPalindrome("Racecar")     // true
isPalindrome("hello")       // false
isPalindrome("a")           // true

```

---

6. `factorial(int n): long`

**Parameters**:       assertEquals(6, factorial(3));

```java
5 × 4 × 3 × 2 × 1 = 120
```



