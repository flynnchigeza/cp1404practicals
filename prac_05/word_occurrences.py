"""
program to count the occurrences of words in a string.
estimate: 3 seconds
a
"""

from collections import defaultdict

word_to_count = defaultdict(int)  # default value of int is 0
text = "this is a collection of words of nice words this is a fun thing it is"
words = text.split()

for word in words:
    word_to_count[word] += 1

max_length = max(len(word) for word in words)
for word in sorted(word_to_count):
    print(f"{word:{max_length}} : {word_to_count[word]}")
