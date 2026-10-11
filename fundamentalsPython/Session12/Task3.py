durations = [3, 4, 5, 2, 6]

seconds = list(map(lambda minutes: minutes * 60, durations))

print("Durations in seconds:", seconds)