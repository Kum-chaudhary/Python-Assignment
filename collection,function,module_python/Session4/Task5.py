call_durations = (12, 5, 0, 20, 7, 3, 15)

duration_list = list(call_durations)

filtered_list = [minutes for minutes in duration_list if minutes >= 5]

result = tuple(filtered_list)

print(result)