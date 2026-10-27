"""
class movie:
    def __init__(self,title,rating):
        title = title
        rating = rating

m = movie("Jawan",4.6)
print(m.title,m.rating) 
"""

class movie:
    def __init__(self,title,rating):
        self.title = title
        self.rating = rating

m = movie("Jawan",4.7)
print(m.title,m.rating)
