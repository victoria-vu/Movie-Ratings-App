"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db

#Functions start here!

# This connects to the database when run curd.py interactively 
if __name__ == '__main__':
    from server import app
    connect_to_db(app)


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user


def login_user(email, password):
    """Return user ID if email and password exists."""

    current_id = User.query.filter(User.email == email).first()
    
    # If current_id
    # Check if password is correct for current_id
            # Return user_id

    if current_id:
        if current_id.password == password:
            return current_id.user_id    
    return False
    

def get_users():
    """Returns all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Returns user by ID."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user with email if it exists."""

    return User.query.filter(User.email == email).first()


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""
    
    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)
    
    return movie


def get_movies():
    """Return all movies."""

    return Movie.query.all()


def get_movie_by_id(movie_id):
    """Returns movie by ID."""
    
    return Movie.query.get(movie_id)


def create_rating(user, movie, score):
    """Create and return a new rating."""

    rating = Rating(user=user, movie=movie, score=score)

    return rating


