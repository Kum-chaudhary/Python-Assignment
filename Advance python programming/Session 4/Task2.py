class songAlreadyExistError(Exception):
    pass
def add_song(song_name,playlist):
    if song_name in playlist:
        raise songAlreadyExistError("Song already exist in playlist !")
    else:
        playlist.append(song_name)
        print("Song added succesfully !")

playlist = ["Perfect","Behavoiur"]

try:
    add_song("Perfect",playlist)
except songAlreadyExistError as e:
    print(e)
print(playlist)
