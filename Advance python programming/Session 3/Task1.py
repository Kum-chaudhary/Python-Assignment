def get_Song_duration(song_name):
    songs = {
        "shape of you" : "3:54",
        "Perfect" : "4:34",
        "O sanam" : "3:56"
    }

    try:
        print("song Duration : ",songs[song_name])
    except KeyError:
        print("song not found in spotify !")

get_Song_duration("Perfect")
get_Song_duration("Hello")        