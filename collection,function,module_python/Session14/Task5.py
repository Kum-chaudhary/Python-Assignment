from collections import defaultdict

playlists = defaultdict(lambda: defaultdict(list))

playlists["user1"]["Favourites"].extend(
    ["Song1", "Song2"]
)

playlists["user2"]["Chill"].append("Song3")

print(dict(playlists))