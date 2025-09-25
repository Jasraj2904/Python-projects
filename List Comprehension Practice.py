# 1. Squares of numbers 1–10
squares = [x**2 for x in range(1, 11)]

# 2. Even numbers from 1–20
evens = [x for x in range(1, 21) if x % 2 == 0]

# 3. Words starting with 'a' from a list
words = ["apple", "banana", "avocado", "grapes"]
a_words = [w for w in words if w.startswith("a")]
