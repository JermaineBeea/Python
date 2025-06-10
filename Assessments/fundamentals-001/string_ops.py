""""### String Operations

`string_ops.py`.

Create this file with the following functionality:

- A function to count vowels in a string: `count_vowels(text: str) -> int`

    - Example: `count_vowels("Zakumi") -> 3`

- A function that reverses each word in a sentence: `reverse_each_word(sentence:str) -> str`

    - Example: `reverse_each_word("hello world") -> "olleh dlrow"`

---
"""""

def count_vowels(text: str) -> int:
  return int(sum([1 for char in text if char in ['a', 'e', 'i', 'o', 'u']]))


def reverse_each_word(sentence:str) -> str:

  sentence = sentence.split()

  return ' '.join(sent[::-1] for sent in sentence)


