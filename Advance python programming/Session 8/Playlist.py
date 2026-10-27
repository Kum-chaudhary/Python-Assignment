import random
from Songs import song_list

random.shuffle(song_list)
print("Random Playlist:")

for song in song_list:
    print(song)