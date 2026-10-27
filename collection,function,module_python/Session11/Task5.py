
import random

songs = [
    "Kesariya",
    "Apna Bana Le",
    "Tum Hi Ho",
    "Heeriye",
    "Chaleya",
    "Tera Ban Jaunga",
    "Raataan Lambiyan",
    "Shayad"
]

playlist = random.sample(songs, 3)

print("Today's Playlist:")

for song in playlist:
    print(song)
