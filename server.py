"""Server for movie ratings app."""
from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# Replace this with routes and view functions!
@app.route("/")
def homepage():
    """View homepage."""
    
    return render_template("homepage.html")


@app.route("/", methods=["POST"])
def log_in():
    """Log-in a user."""

# Handles submission of the login form on the Homepage 
# Query for user with a given email, make sure passwords match => see crud.py Line 21
# Log user in by adding their primary key to the Flask session
# Tell user they logged in successfully: flash message "Logged in!"

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.login_user(email, password) 
    # Return user_id, so user = user_id
    
    if user:
        session["user"] = user
        flash("You are successfully logged in.")
    else:
        flash("Error! Please create a new account.")

    return redirect("/")   
        


@app.route("/movies")
def all_movies():
    """View all movies."""

    movies = crud.get_movies()

    return render_template("all_movies.html", movies=movies)
# optional task = alphabeticallizing the movies

@app.route("/movies/<movie_id>")
def show_movie(movie_id):
    """Show details on a particular movie."""
    
    movie = crud.get_movie_by_id(movie_id)

    return render_template("movie_details.html", movie=movie)


@app.route("/users")
def all_users():
    """Show all users."""

    users = crud.get_users()
    
    return render_template("all_users.html", users=users)


@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        flash("Account already exist with that email. Try again.")
    else:
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in!")
    
    return redirect("/")


@app.route("/users/<user_id>")
def show_user(user_id):
    """Show details on a particular user"""

    user = crud.get_user_by_id(user_id)
    
    return render_template("user_details.html", user=user)


@app.route("/ratings")
def add_rating():
    """Show form to create a movie rating."""

    movies = crud.get_movies()

    return render_template("ratings.html", movies=movies)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
