with open("plylist.txt","r") as file:
    file.readline() # skip first song
    file.readline() # skip second song

    song = file.readline()
    print("Third song :",song.strip())