def display_frd(friends):
    for username,folloers in friends.items():
        print(f"{username} {folloers} followers")

instagram_frds ={
    "Kumkum" : "2.3k",
    "riddhi" : "5.6k",
    "kajal": "3.6k"
}        

display_frd(instagram_frds)