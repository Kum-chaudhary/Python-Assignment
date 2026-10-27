ipl = {}

ipl["CSK"] = {
    "Ruturaj" : 75,
    "Dhoni" : 78,
    "Jadeja" : 60
}

ipl["MI"] = {
    "rohit" : 60,
    "surya" : 65,
    "Hardik" : 30
}

player = "rohit"
team = "MI"

print("Team :",team)
print("Player:",player)
print("Runs :",ipl[team][player])