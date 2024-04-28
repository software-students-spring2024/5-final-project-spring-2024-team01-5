from flask import Flask, render_template, request, redirect, flash
from flask_cors import CORS
from pymongo import MongoClient
from flask_pymongo import PyMongo
from functions import calculate_final_exam_grade, calculate_GPA
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

'''
# DB Set up
# TODO: Change these collection and db names if needed
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
client = MongoClient(F"mongodb+srv://{DB_USER}:{DB_PASSWORD}@cluster0.gpzcbbz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["GPAlCalculator"]
collection = db["grades"]
'''

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
    
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_CONNECTION = F"mongodb+srv://{DB_USER}:{DB_PASSWORD}@cluster0.gpzcbbz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    app.config['MONGO_URI'] = DB_CONNECTION
    client = PyMongo(app).cx["GPAlCalculator"]
    collection = client.db.grades

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
            semester = data["semester"]
            instructor = data["instructor"]
            # print(course_name, course_grade, course_credits)
            # Add a flash message
            flash(f"Grade {course_grade} for {course_name} {semester} added successfully", "success")
            # Save grade to DB
            grade = {
                "course_name": course_name,
                "course_grade": course_grade,
                "course_credits": course_credits,
                "semester": semester,
                "instructor": instructor
            }
            print(grade)
            collection.insert_one(grade)
            print("Grade added to DB")
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
        print("Fetching grades from DB")
        grades = collection.find()
        
        # create list of grade to credit dictionary for GPA calculation
        courses = []
        for grade in grades:
            courses.append([grade["course_grade"], grade["course_credits"], grade["course_name"], grade["semester"], grade["instructor"]])
        print(courses)
        gpa = calculate_GPA(courses)
        gpa = round(gpa, 3) 
        print(gpa)
        
        return render_template("view_grades.html", section="View All Grades", gpa=gpa, courses=courses)
    
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