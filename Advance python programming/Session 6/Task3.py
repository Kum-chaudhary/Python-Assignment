class user:
    def __init__(self,username,email):
        self.username = username
        self.email = email

class influencer(user):
    def __init__(self, username, email,follower):
        super().__init__(username, email)        
        self.follower = follower

class VerifiedInfluencer(influencer):
    def __init__(self, username, email, follower,badge):
        super().__init__(username, email, follower) 
        self.badge = badge

user1 = VerifiedInfluencer("Kumkum","kumkum3820@gmail.com",1500,"blue tick")

print("Username :",user1.username)
print("Email :",user1.email)
print("Follower:",user1.follower)
print("Badge :",user1.badge)