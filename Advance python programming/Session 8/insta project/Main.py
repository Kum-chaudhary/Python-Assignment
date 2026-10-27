from insta_utils.likes import like_count
from insta_utils.comment import comment_count

likes = 100
comments = 20

likes = like_count(likes,5)
comments = comment_count(comments,3)

print("total like :",likes)
print("Total comment:",comments)
