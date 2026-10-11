team = {
    "CSK": {
        "captain": "Dhoni",
        "players": 18
    },
    "MI": {
        "captain": "Rohit",
        "players": 17
    }
}

# Add a new team
team["GT"] = {
    "captain": "Hardik",
    "players": 16
}

# Print all team names and captains
for team_name, details in team.items():
    print("Team:", team_name)
    print("Captain:", details["captain"])