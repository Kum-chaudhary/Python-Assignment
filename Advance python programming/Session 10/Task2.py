from tkinter import*
screen = Tk()
screen.title("My Playlist")
screen.geometry("400x250")

def play():
    Lbl.config(Text="Playing")

def pause():
    Lbl.config(Text="Paused")

def next_song():
    Lbl.config(text="Next song")    

btn1 = Button(screen,text="Play",command=play).pack(pady=5)

btn2 = Button(screen,text="Pause").pack(pady=5)

btn3 = Button(screen,text="Next").pack(pady=5)

Lbl = Label(screen,text="Select an action")
Lbl.pack(pady=10)

screen.mainloop()