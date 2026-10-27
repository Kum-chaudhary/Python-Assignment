from Task1 import add_song, remove_song,display_playlist

playlist = []

# add songs
playlist = add_song("kalja ni vat",playlist)
playlist = add_song("jid",playlist)
playlist = add_song("fana",playlist)

print("playlist after adding songs:")
display_playlist(playlist)

# remove song

playlist = remove_song("jid",playlist)

print("\n playlist after removing song:")
display_playlist(playlist)

