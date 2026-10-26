file = open("my_fav_songs.txt", "r")
songs = file.readlines()
for song in songs:
    print(song.strip())

total_song = len(songs)

print("total song :",total_song)
file.close()    