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
        if username in cls.users:
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
        if username in cls.users and cls.users.get(username).__password == hash(password):
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

    @classmethod
    def add_movie(cls):
        title = input("Enter the movie title").lower()
        showtime = input("Enter the showtime").lower()
        total_seats = input("Enter the total number of seats: ")
        cls.movie.append(Movie(title, showtime, total_seats))
        print("Movie has been successfully added!!")


def main():
    admin = Admin(input("Set the admin password!!"))

    print("Movie Booking System!!")
    while 1:
        print("\n1) Register\n2) Login\n3) Admin \n4) Logout")
        choice = int(input("Enter the choice: "))

        if choice == 1:
            User.register()
        elif choice == 2:
            user = User.login()
            if user:
                print("Booking Menu!!")
                while 1:
                    print("\n1) View Movie\n2) Book Movie\n3) View Booking\n4) Go to Main menu")
                    user_choice = int(input("Enter your choice"))
                    if user_choice == 1:
                        if admin.get_movies():
                            movie.display_details()
                    elif user_choice == 2:
                        if not admin.get_movies():
                            print("No movies available!!")
                            continue
                        movie_tite = input("Enter the Movie Title: ").lower()
                        for movie in admin.get_movies():
                            if movie.title == movie_tite:
                                if movie.available_seats > 0:
                                    print(f"Available Seats: {movie.available_seats}")
                                    seats_to_book = int(input("Enter the number of seats: "))
                                    if movie.available_seats >= seats_to_book:
                                        movie.available_seats -= seats_to_book
                                        booking = Booking(user, movie, seats_to_book)
                                        user.add_booking(booking)
                                        print("Booking Successfull!!")
                                    else:
                                        print("Not sufficient seats available!!")
                                else:
                                    print("Housefull!")
                            else:
                                print("Please enter the correct title!!")
                    elif user_choice == 3:
                        if user.get_booking():
                            for booking in user.get_booking():
                                booking.dispay_details()
                        else:
                            print("Time to book your first movie!!")
                    elif user_choice == 4:
                        print("Returning to main menu!!")
                        break
                    else:
                        print("Please enter correct choice!!")
            else:
                print("User not found!")
        elif choice == 3:
            admin_password = input("Enter the admin password: ")
            if hash(admin_password) == Admin.password:
                print("Welcome to the admin dashboard!!")
                while True:
                    print("\n1) Add movie\n2 Delete movie\n3) View Booking\n4) Exit")
                    admin_choice = int(input("Hey Admin enter your choice: "))
                    if admin_choice == 1:
                        admin.add_movie()
                    elif admin_choice == 2:
                        title = input("Enter the movie title you want to delete: ")
                        if len(admin.movie) == 0:
                            print("No Movies availabe")
                            continue
                        for i in range(len(admin.movie)):
                            if admin.movie[i].title == title:
                                admin.movie.pop(i)
                                print("Movie has been successfully deleted")
                                break
                    elif admin_choice == 3:
                        if admin.get_movies():
                            for movie in admin.get_movies():
                                movie.display_details()
                        else:
                            print("Add new movies!!")
                    elif admin_choice == 4:
                        print("Logging out of admin!!")
                        break
                    else:
                        break
        elif choice == 4:
            print("Thanks for using the movie booking system!!")
            break
        else:
            print("You have the wrong choice\nPlease Enter again!!")

main()