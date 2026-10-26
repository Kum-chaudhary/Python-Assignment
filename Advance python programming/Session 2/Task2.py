def read_next_line(filename):
    with open(filename,"r") as file:
        file.seek(20)
        line = file.readline()
        print("Next Line :",line)
read_next_line("lyrics.txt")        