"""Module providing framework for the web app."""
from flask import Flask, render_template, request, redirect, flash
from flask_cors import CORS
from pymongo import MongoClient
from functions import calculate_final_exam_grade, calculate_GPA, calculate_course_grade
import json
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
        return render_template("index.html", section="Home")
    

    @app.route("/add_grade", methods=["GET", "POST"])

    def add_grade():
        """
        Route for the add course page.
        """

        if request.method == "POST":
            # Handle the POST request
            # Add the grade to the database or perform any other necessary actions
            data = request.form
            # SAVE THIS DATA INTO MONGODB
            course_name = data["course_name"]
            course_grade = data["course_grade"]
            course_credits = data["course_credits"]
            # print(course_name, course_grade, course_credits)
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

        # Fetch the grades from MongoDB using find({user_id: user_id}), after we add auth
        # before we add auth, we can test by fetching all data
        return render_template("view_grades.html", section="View All Grades")
    
    @app.route("/calculate", methods=["GET", "POST"])
    def calculate():
        """
        Route for the calculate GPA page.
        """
        if request.method == "POST":
            data = request.data
            print(data)
            data = json.loads(data)

            current_grade = float(data["current_grade"])
            final_weight = float(data["final_weight"])
            target_grade = float(data["target_grade"])
            final_grade_needed = calculate_final_exam_grade(current_grade, final_weight, target_grade) # change this to calculate grade later
             # Round to 2 decimal places
            final_grade_needed = round(final_grade_needed, 2)
            response = {
                "final_grade": final_grade_needed
            }
            return response  # Return the calculated response
        else:
            # calculate final grade of a class based on the weights of each section
            return render_template("calculate.html", section="Calculate Final Grade")

    return app