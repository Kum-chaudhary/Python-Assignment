class user:
    def __init__(self,username,email):
        self.username = username
        self.email = email

class influencer(user):
    def __init__(self, username, email,follower):
        super().__init__(username, email)
        self.follower = follower

influencer1 = influencer("Kumkum","kumkum3820@gmail.com",1500)
print("Username :",influencer1.username)
print("Email :",influencer1.email)
print("Followers :",influencer1.follower)                