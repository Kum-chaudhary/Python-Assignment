def book_movie_ticket(tickets):
    wallet_balance = 1000

    try:
        price_per_ticket = wallet_balance / tickets

        print("Price per ticket :",price_per_ticket)

    except ZeroDivisionError:
        print("Error : number of ticket cannot be zero !")

    except ValueError:
        print("Error : Enter valid number!")
try:
    tickets = int(input("Enter your ticket:"))
    book_movie_ticket(tickets)

except ValueError:
    print("Error : please enter a valid number")

    
