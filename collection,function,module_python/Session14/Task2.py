playlists = {}

def add_song_to_playlist(playlists, user,playlist_name,song_title,artist):
    playlists.setdefault(user,{})

    playlists[user].setdefault(playlist_name,[])

    song = {
        "Title" : song_title,
        "artist" : artist
    }

    playlists[user][playlist_name].append(song)

    print("song added sucessfully !")


add_song_to_playlist(playlists,"kumkum","Favorite","Perfect","Ed sheeran")
add_song_to_playlist(playlists,"kumkum","Chill","Shape of you","Ed sheeran")
add_song_to_playlist(playlists,"minal","Favorite","Believe","Dragons")

print(playlists)