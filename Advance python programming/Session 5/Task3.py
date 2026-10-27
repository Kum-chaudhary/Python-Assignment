class InstagramPost:
    def __init__(self,caption,like,comment):
        self.caption = caption
        self.like = like
        self.comment = comment

    def add_comment(self,comment_text):
            self.comment.append(comment_text)
            self.like += 1

    def show_post(self):
         print("Caption :",self.caption)
         print("Like :",self.like)
         print("Comment :",self.comment)

post = InstagramPost("Beautiful day !",10,["Nice pic","Awesome"])
post.add_comment("Amazing!")
post.show_post()         
            
