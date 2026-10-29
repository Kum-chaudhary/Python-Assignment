from tkinter import*
screen = Tk()
screen.title("Button Grid")
screen.geometry("400x250")
btn1 = Button(screen,text="Like").grid(row=0,column=0,padx=10,pady=10)
btn2 = Button(screen,text="share").grid(row=0,column=1,padx=10,pady=10)
btn3 = Button(screen,text="Download").grid(row=1,column=0,padx=10,pady=10)
btn4 = Button(screen,text="Add to Game").grid(row=1,column=1,padx=10,pady=10)

screen.mainloop()