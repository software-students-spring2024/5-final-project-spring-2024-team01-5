"""Module providing framework for the web app."""
from flask import Flask, render_template, request, redirect, flash
from flask_cors import CORS
from pymongo import MongoClient

# DB Set up
# TODO: Change these collection and db names if needed

client = MongoClient("mongodb://localhost:27017/")
db = client["GPACalculator"]
collection = db["grades"]


def create_app(test_config=None):
    """
    Create and configure the Flask application.

    Args:
        test_config (dict, optional): Configuration dictionary for testing purposes. Defaults to None.

    Returns:
        Flask: The configured Flask application.
    """
    app = Flask(__name__)
    app.secret_key = "secret_key"  # Set the secret key for flash messages
    CORS(app) # Enable CORS for all routes
    if test_config is not None:
        app.config.update(test_config)

    @app.route("/")
    def home():
        """
        Route for the home page.
        """
        return render_template("index.html")
    

    @app.route("/add_grade", methods=["GET", "POST"])

    def add_grade():
        """
        Route for the add course page.
        """

        if request.method == "POST":
            # Handle the POST request
            # Add the grade to the database or perform any other necessary actions
            data = request.form
            course_name = data["course_name"]
            course_grade = data["course_grade"]
            print(course_name, course_grade)
            # Add a flash message
            flash(f"Grade {course_grade} for {course_name} added successfully", "success")
            return redirect(request.url)
        else:
            # Handle the GET request
            return render_template("add.html", section="Add Course Grade")
    
    @app.route("/view_grades")
    def view_grades():  
        """
        Route for the view grades page.
        """

        # Fetch the grades from the database
        # when we add auth, find using user id
        return render_template("view_grades.html")
    
    @app.route("/calculate")
    def calculate():
        """
        Route for the calculate GPA page.
        """
        # calculate final grade of a class based on the weights of each secrtion
        return render_template("calculate.html")

    return app