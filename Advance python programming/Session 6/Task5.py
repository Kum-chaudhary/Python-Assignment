class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class Influencer(User):
    def __init__(self, username, email, followers):
        super().__init__(username, email)
        self.followers = followers

class VerifiedInfluencer(Influencer):
    def __init__(self, username, email, follower,badge):
        super().__init__(username, email, follower) 
        self.badge = badge

    def format_follower(self):
        if self.followers >= 1_000_000:
            return f"{self.followers / 1_000_000:.1f}M"
        elif self.followers >= 1_000:
            return f"{self.followers / 1_000:.1f}K"
        else:
            return str(self.followers)

    def display_profile(self):
        print("Instagram Profile")
        print("-----------------")
        print("Username :",self.username)
        print("Follower :",self.format_follower())
        print("Badge Status :",self.badge)

user1 = VerifiedInfluencer("Kumkum","Kumkum3820@gmail.com",1500,"verified")

user1.display_profile()

        
        
