file = open("my_fav_songs.txt", "r")
for line_num, song in enumerate(file, start=1):
    print(line_num,song.strip())

file.close()
