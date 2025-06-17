"""
Word Occurrences
Estimate: 20 minutes
Actual:   32 minutes
"""

word_to_count = {}
text = input("Enter text: ")
words = text.split()
for word in words:
    count = word_to_count.get(word, 0)
    word_to_count[word] = count + 1

print(words)
print(word_to_count)