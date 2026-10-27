

from Task1 import add_song, remove_song

playlist = []

playlist = add_song("Kesariya", playlist)
playlist = add_song("Shape of You", playlist)
playlist = add_song("Believer", playlist)

playlist = remove_song("Shape of You", playlist)

print("Updated Playlist:", playlist)