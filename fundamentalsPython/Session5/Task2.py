# Count characters excluding spaces
user_bio = "Music lover | Foodie | Traveller"
count = 0

for char in user_bio:
    if char != " ":
        count = count + 1
print("number of character excluding spaces:",count)

"""
output:
number of character excluding spaces: 27
"""