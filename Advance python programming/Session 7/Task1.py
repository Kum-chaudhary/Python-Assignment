# method overridding

class InstaStory:
    def Share(self):
        print("Sharing in image story")

class WhatsappStory(InstaStory):
    def Share(self):        
        print("sharing a text status")

obj1 = InstaStory()
obj2 = WhatsappStory()

obj1.Share()
obj2.Share()