# my app is going to be a movie collection app.
# all references in refrence fill in repository

# first import flask and other tools needed to create the app
# then create the app and set up the database connection
# sqlite lets python work nia sqlite database 

from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = "movies.db" # set database name


def get_db_connection(): # this is function to open and connect to the database
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def create_table(): # this creates the movies table, with columns for id, title, genre, year, and rating
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            genre TEXT NOT NULL,
            year INTEGER NOT NULL,
            rating INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()  # to close the connection after creating the table


@app.route("/")   # to make main homepage , this will render the index.html template
def home():
    return render_template("index.html")


@app.route("/movies", methods=["GET"]) # for the GET request , to fetch all , get all movies from the database 
def get_movies():
    conn = get_db_connection()
    movies = conn.execute("SELECT * FROM movies").fetchall()
    conn.close()

    return jsonify([dict(movie) for movie in movies]) # to convert the movie data into a list of dictionaries and return it as a JSON response


@app.route("/movies", methods=["POST"]) # now to add a new movie to the database,
def add_movie():
    data = request.get_json()

    title = data["title"]
    genre = data["genre"]
    year = data["year"]
    rating = data["rating"]

    conn = get_db_connection() # ?? is used as temporary value until the actual value is entered, prevents issues !
    conn.execute(
        "INSERT INTO movies (title, genre, year, rating) VALUES (?, ?, ?, ?)",
        (title, genre, year, rating)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Movie added successfully"})


@app.route("/movies/<int:movie_id>", methods=["PUT"]) # to update and existing movie value 
def update_movie(movie_id):
    data = request.get_json()

    title = data["title"]
    genre = data["genre"]
    year = data["year"]
    rating = data["rating"]

    conn = get_db_connection()
    conn.execute(
        "UPDATE movies SET title = ?, genre = ?, year = ?, rating = ? WHERE id = ?",
        (title, genre, year, rating, movie_id)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Movie updated successfully"}) # runs this message if the update has been successful


@app.route("/movies/<int:movie_id>", methods=["DELETE"]) # to delete movie from database 
def delete_movie(movie_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Movie deleted successfully"})# message show if the delete has been successful


if __name__ == "__main__":
    create_table()
    app.run(debug=True)# now this runs the app, the create table function is run to make sure the movei table has been created before start




# also must create templete folder and index.html file to render the homepage, this will be the user interface for the movie collection app.
# do this before running app

# to test in teminal run pip install flask
# then c:\Users\Cheryl\OneDrive\Desktop\.venv\Scripts\python.exe -m pip install flask (for my PC)
# if successful will return:Running on http://127.0.0.1:5000

# will show the home page of app , nothing in it right now

#added new template to folder and added html code to index.html
# https://chatgpt.com/c/6a00bb0c-6538-83eb-bab1-9f16f376b61f
# now when you run the app and go to the homepage,
# you should see the movie collection interface where you can add, view, update, and delete movies from your collection.