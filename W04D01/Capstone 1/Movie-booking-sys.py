"""
Features:
    1.	User Registration and Login:
        o	Users can register and log in to book tickets.
        o	Credentials are stored securely in memory.
    2.	Movie and Show Management:
        o	Admin can add movies and show timings.
        o	Users can view available movies and their timings.
    3.	Seat Booking:
        o	Users can select a movie, showtime, and book seats.
        o	Seats are dynamically updated based on availability.
    4.	Booking History:
        o	Users can view their past bookings.

Class Design:
    1.	User: Handles user details, login, and registration.
    2.	Movie: Stores information about movies, showtimes, and available seats.
    3.	Booking: Manages booking information, such as movie, user, and seat details.
    4.	Admin: Manages movie and showtime additions.
"""


class User:
    """
    User:
       Handles user details, login, and registration.
    """
    users = {}
    def __init__(self, name, phno, username, password):
        self.__name = name
        self.__phno = phno
        self.__username = username
        self.__password = hash(password)
        self.__booking = []
    
    # HW: Create getter an setter method for required the attribute
    def get_booking(self):
        return self.__booking
    
    def add_booking(self, booking):
        self.__booking.append(booking)

    def get_name(self):
        return self.__name
    
    @classmethod
    def register(cls):
        name = input("Enter the name: ")
        phn_no = input("Enter the phone no: ")
        username = input("Enter the username: ")
        if username in cls.user:
            print("Username already exists!!")
            return None
        password = input("Enter the password: ")
        cls.users[username] = User(name, phn_no, username, password) # User.users[username] = blahblah in case of statci method
        print("Resgistartion Successfull!!")
        return True
    
    @classmethod
    def login(cls):
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        if username in cls.user and cls.users.get(username).password == hash(password):
            print("Login Successfull!!")
            return cls.users[username]
        print("Username or Password not correct!!")
        return None
    

class Movie:
    """
    Movie: 
        Stores information about movies, showtimes, and available seats.
    """
    def __init__(self, title, showtime, total_seating):
        self.title = title
        self.showtime = showtime
        self.total_seating = int(total_seating)
        self.available_seat = self.total_seating
    
    def display_details(self):
        print(f"Movie: {self.title} | Showtime: {self.showtime} | Seats Available: {self.available_seat}")


class Booking:
    """
    Booking: 
        Manages booking information, such as movie, user, and seat details.
    """
    def __init__(self, user, movie, seats_booked):
        self.user = user
        self.movie = movie
        self.seats_booked = int(seats_booked)
    
    def display_details(self):
        print(f"User: {self.user.get_name()} | Movie: {self.movie.title} | Showtime: {self.movie.showtime}"
              f"Seats Booked: {self.seats_booked}")


class Admin:
    """
    Admin: 
        Manages movie and showtime additions.
    """    
    movie = []
    password = ""
    def __init__(self, password):
        self.set_admin_password(password)

    @classmethod
    def set_admin_password(cls, password):
        cls.password = hash(password)
    
    @classmethod
    def get_movies(cls):
        return cls.movie