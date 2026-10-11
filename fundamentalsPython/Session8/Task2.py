# extra artist name
def extra_artist(song_title):
    dash = song_title.index("-")
    artist = song_title[dash + 1:]
    return artist.strip() # remove extra space

song = "perfect  - Ed shreeran"
print("artist name:",extra_artist(song))
