class InvalidSeatNumberError(Exception):
    pass
def book_ticket(movie,seat_number):
    if seat_number <= 0:
        raise InvalidSeatNumberError("Seat number must be positive !")
    else:
        print("ticket book successfully",movie)

try:
    book_ticket("Avenger",-2)
except InvalidSeatNumberError as e:
    print(e)
