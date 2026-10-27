class content:
    def display(self,title):
        print("Title :",title)
class Movie(content):
    def display(self, title,year):
        print("Title:",title)
        print("Year:",year)

obj = Movie()
obj.display("3 Idiot",2009)


                
