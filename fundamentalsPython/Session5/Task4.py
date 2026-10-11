# Print only vowels from a word

word = input("Enter a word:")
for char in word:
    if char == "a" or char == "e" or char == "i" or char == "o"or char == "u":
        print(char)

"""
output:
Enter a word:kevin
e
i
"""
