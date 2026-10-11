def video_views(titles, views):
    return [(title, round(view, -3))
            for title, view in zip(titles, views)]


titles = ["Python Tutorial", "C Programming", "Web Development"]
views = [12567, 23456, 98765]

result = video_views(titles, views)

print(result)