""" word occurrences
Estimate : 20 minutes
Actual: 30 minutes """

text = input ("Enter the text:")
words = text.split()
word_counts = {}

for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

# for word in words:
#   word = word.lower()
#   if word in word_counts:
#       word_counts[word] += 1
#   else:
#       word_counts[word] = 1

sorted_words = sorted(word_counts.keys())
max_length = max(len(word) for word in sorted_words)

for word in sorted_words:
    print(f"{word:{max_length}}:{word_counts[word]}")


