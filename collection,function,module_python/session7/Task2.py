import string

review = """
Zomato is a good food delivery app.
Zomato delivers food quickly and good food makes me happy.
"""

review = review.lower()

for char in string.punctuation:
    review = review.replace(char, "")

words = review.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)