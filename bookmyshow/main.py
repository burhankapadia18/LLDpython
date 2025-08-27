from enums.city import City
from enums.seat_category import SeatCategory
from movie_controller import MovieController
from theatre_controller import TheatreController
from seat import Seat
from booking import Booking
from theatre import Theatre
from screen import Screen
from show import Show
from movie import Movie


class BookMyShow:
    """
    Main application class for the BookMyShow movie booking system.
    
    This class orchestrates the entire movie booking process including:
    - Movie management through MovieController
    - Theatre management through TheatreController
    - Booking creation and seat selection
    - System initialization with sample data
    
    The class follows a simplified booking flow where users can:
    1. Search for movies by city
    2. Select a movie
    3. Choose from available shows
    4. Select seats
    5. Complete booking
    """

    movie_controller: MovieController
    theatre_controller: TheatreController

    def __init__(self):
        """
        Initialize the BookMyShow application.
        
        Creates instances of MovieController and TheatreController to manage
        movies and theatres respectively.
        """
        self.movie_controller = MovieController()
        self.theatre_controller = TheatreController()

    def create_booking(self, user_city: City, movie_name: str):
        """
        Create a movie booking for a user.
        
        This method implements the complete booking flow:
        1. Search for movies available in the user's city
        2. Find the specific movie requested by the user
        3. Get all shows for that movie in the city
        4. Select a show (currently picks the first available)
        5. Check seat availability and book if available
        6. Create a booking record
        
        Args:
            user_city (City): The city where the user wants to book
            movie_name (str): Name of the movie to book
            
        Note:
            This is a simplified implementation that automatically selects
            the first available show and seat 30. In a real system, users
            would choose these interactively.
        """
        # 1. search movie by my location
        movies = self.movie_controller.get_movies_by_city(user_city)

        # 2. select the movie which you want to see. i want to see Baahubali
        interested_movie = None
        for movie in movies:
            if movie.get_movie_name() == movie_name:
                interested_movie = movie

        # 3. get all show of this movie in Bangalore location
        shows_theatre_wise = self.theatre_controller.get_all_show(interested_movie, user_city)

        # 4. select the particular show user is interested in
        entry = list(shows_theatre_wise.items())[0]
        running_shows = entry[1]
        interested_show = running_shows[0]

        # 5. select the seat
        seat_number = 30
        booked_seats = interested_show.get_booked_seat_ids()
        if seat_number not in booked_seats:
            booked_seats.append(seat_number)
            # start payment
            booking = Booking()
            my_booked_seats = []
            for screen_seat in interested_show.get_screen().get_seats():
                if screen_seat.get_seat_id() == seat_number:
                    my_booked_seats.append(screen_seat)
            booking.set_booked_seats(my_booked_seats)
            booking.set_show(interested_show)
        else:
            # throw exception
            print("seat already booked, try again")
            return

        print("BOOKING SUCCESSFUL")

    def initialize(self):
        """
        Initialize the system with sample data.
        
        This method sets up the initial state of the system by:
        1. Creating sample movies (Avengers, Baahubali)
        2. Creating theatres with screens, seats, and shows
        3. Adding movies to different cities
        4. Setting up theatre-shows mapping
        
        This is typically called once when the system starts up.
        """
        # create movies
        self.create_movies()

        # create theater with screens, seats and shows
        self.create_theatre()

    def create_theatre(self):
        """
        Create sample theatres with screens, seats, and shows.
        
        Creates two theatres (INOX and PVR) in different cities with:
        - Multiple screens per theatre
        - 100 seats per screen (40 Silver, 30 Gold, 30 Platinum)
        - Multiple shows per screen for different movies
        - Different show timings (morning and evening)
        
        The theatres are added to the theatre controller for city-based lookup.
        """
        avenger_movie = self.movie_controller.get_movie_by_name("AVENGERS")
        baahubali = self.movie_controller.get_movie_by_name("BAAHUBALI")

        inox_theatre = Theatre()
        inox_theatre.set_theatre_id(1)
        inox_theatre.set_screens(self.create_screen())
        inox_theatre.set_city(City.Bangalore)
        inox_shows = []
        inox_morning_show = self.create_shows(1, inox_theatre.get_screens()[0], avenger_movie, 8)
        inox_evening_show = self.create_shows(2, inox_theatre.get_screens()[0], baahubali, 16)
        inox_shows.append(inox_morning_show)
        inox_shows.append(inox_evening_show)
        inox_theatre.set_shows(inox_shows)

        pvr_theatre = Theatre()
        pvr_theatre.set_theatre_id(2)
        pvr_theatre.set_screens(self.create_screen())
        pvr_theatre.set_city(City.Delhi)
        pvr_shows = []
        pvr_morning_show = self.create_shows(3, pvr_theatre.get_screens()[0], avenger_movie, 13)
        pvr_evening_show = self.create_shows(4, pvr_theatre.get_screens()[0], baahubali, 20)
        pvr_shows.append(pvr_morning_show)
        pvr_shows.append(pvr_evening_show)
        pvr_theatre.set_shows(pvr_shows)

        self.theatre_controller.add_theatre(inox_theatre, City.Bangalore)
        self.theatre_controller.add_theatre(pvr_theatre, City.Delhi)

    def create_screen(self):
        """
        Create a screen with seats.
        
        Returns:
            List[Screen]: A list containing one screen with 100 seats
                         (40 Silver, 30 Gold, 30 Platinum)
        """
        screens = []
        screen1 = Screen()
        screen1.set_screen_id(1)
        screen1.set_seats(self.create_seats())
        screens.append(screen1)

        return screens

    def create_shows(self, show_id, screen, movie, show_start_time):
        """
        Create a show for a specific movie on a specific screen.
        
        Args:
            show_id (int): Unique identifier for the show
            screen (Screen): The screen where the show will be displayed
            movie (Movie): The movie to be shown
            show_start_time (int): Start time in 24-hour format (e.g., 8 for 8 AM, 16 for 4 PM)
            
        Returns:
            Show: A configured show object
        """
        show = Show()
        show.set_show_id(show_id)
        show.set_screen(screen)
        show.set_movie(movie)
        show.set_show_start_time(show_start_time)  # 24 hrs time ex: 14 means 2pm and 8 means 8AM
        return show

    def create_seats(self):
        """
        Create 100 seats for a screen with different categories.
        
        Creates a total of 100 seats distributed as:
        - Seats 1-40: SILVER category
        - Seats 41-70: GOLD category  
        - Seats 71-100: PLATINUM category
        
        Returns:
            List[Seat]: List of 100 seat objects with appropriate categories
        """
        # creating 100 seats for testing purpose, this can be generalised
        seats = []

        # 1 to 40 : SILVER
        for i in range(40):
            seat = Seat()
            seat.set_seat_id(i)
            seat.set_seat_category(SeatCategory.SILVER)
            seats.append(seat)

        # 41 to 70 : GOLD
        for i in range(40, 70):
            seat = Seat()
            seat.set_seat_id(i)
            seat.set_seat_category(SeatCategory.GOLD)
            seats.append(seat)

        # 71 to 100 : PLATINUM
        for i in range(70, 100):
            seat = Seat()
            seat.set_seat_id(i)
            seat.set_seat_category(SeatCategory.PLATINUM)
            seats.append(seat)

        return seats

    def create_movies(self):
        """
        Create sample movies and add them to different cities.
        
        Creates two movies:
        - Avengers (128 minutes duration)
        - Baahubali (180 minutes duration)
        
        Both movies are added to Bangalore and Delhi cities for demonstration.
        """
        # create Movies1
        avengers = Movie()
        avengers.set_movie_id(1)
        avengers.set_movie_name("AVENGERS")
        avengers.set_movie_duration(128)

        # create Movies2
        baahubali = Movie()
        baahubali.set_movie_id(2)
        baahubali.set_movie_name("BAAHUBALI")
        baahubali.set_movie_duration(180)

        # add movies against the cities
        self.movie_controller.add_movie(avengers, City.Bangalore)
        self.movie_controller.add_movie(avengers, City.Delhi)
        self.movie_controller.add_movie(baahubali, City.Bangalore)
        self.movie_controller.add_movie(baahubali, City.Delhi)


def main():
    """
    Main entry point for the BookMyShow application.
    
    Demonstrates the booking system by:
    1. Creating a BookMyShow instance
    2. Initializing the system with sample data
    3. Creating two sample bookings for the same movie
    """
    book_my_show = BookMyShow()
    book_my_show.initialize()

    # user1
    book_my_show.create_booking(City.Bangalore, "BAAHUBALI")
    # user2
    book_my_show.create_booking(City.Bangalore, "BAAHUBALI")


if __name__ == "__main__":
    main()