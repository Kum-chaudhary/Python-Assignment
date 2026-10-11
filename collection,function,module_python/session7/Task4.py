import string

text = "The food is good and the delivery is fast in the city."

stopwords = ["the", "and", "in", "of", "a", "to", "is"]

text = text.lower()

for char in string.punctuation:
    text = text.replace(char, "")

words = text.split()
word_count = {}

for word in words:
    if word not in stopwords:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

print(word_count)