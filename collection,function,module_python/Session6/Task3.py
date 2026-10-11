teams = ["CSK", "MI", "RCB", "KKR", "GT"]
points = [12, 8, 15, 10, 14]

team_points = dict(zip(teams, points))

for team, point in team_points.items():
    if point > 10:
        print(team, point)