playlists = [[210,180,240],[150,200],[300,120,90]]

duration = [song for playlist in playlists for song in playlist if song > 200]

print(duration)