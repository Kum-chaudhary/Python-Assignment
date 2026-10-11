def book_movie_ticket(movie_name, seat_type="Regular", snacks=None):
    print("Movie Name:", movie_name)
    print("Seat Type:", seat_type)
    print("Snacks:", snacks)
    print("-" * 30)


# Only positional arguments
book_movie_ticket("Jawan", "Regular", "Popcorn")

# Only keyword arguments
book_movie_ticket(
    movie_name="Pathaan",
    seat_type="VIP",
    snacks="Cold Drink"
)

# Mix of positional and keyword arguments
book_movie_ticket("Jawan", snacks="Popcorn", seat_type="VIP")