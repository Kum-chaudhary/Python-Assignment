import tkinter as tk
screen = tk.Tk()
screen.title("Login Form")
screen.geometry("400x250")

def login():
    user = username.get()
    pwd = password.get()

    if user != "" and pwd != "":
        result.config("Login sucessfully !")
    else:
        result.config("Please fill all field")
        
tk.Label(screen,text="Username").pack(pady=5)
username = tk.Entry(screen)
username.pack()

tk.Label(screen,text="Password").pack(pady=5)
password = tk.Entry(screen,show="*")
password.pack()

tk.Button(screen,text="Login",command=login).pack(pady=15)

result = tk.Label(screen,text="")
result.pack()


screen.mainloop()

