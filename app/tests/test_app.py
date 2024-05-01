# pylint: disable=missing-final-newline,missing-module-docstring,import-error
import pytest
from unittest.mock import patch, MagicMock
from app import create_app

class Tests:
    """
    This class contains test cases for the web app.
    """
    @pytest.fixture()
    def app(self):
        """
        Fixture to set up the app for testing.

        Returns:
            Flask app: The Flask app object.
        """
        app = create_app({
            "TESTING": True,
            "MONGO_URI": "mock_uri"  # use a mock URI
        })
        return app

    @pytest.fixture()
    def client(self, app):
        """
        Fixture to get the test client.

        Args:
            app (Flask app): The Flask app object.

        Returns:
            Flask test client: The Flask test client object.
        """
        return app.test_client()
    
    @pytest.fixture
    def mock_mongodb(self, mocker):
        # Mock the pymongo collection
        mock_collection = MagicMock()
        mocker.patch('pymongo.collection.Collection.insert_one', new=mock_collection.insert_one)
        return mock_collection


    @staticmethod
    def test_sanity_check():
        """
        Test case to check the sanity of the testing framework.
        """
        expected = True
        actual = True
        assert actual == expected

    def test_index_route(self, client):
        """
        Test case to ensure the home route renders correctly.

        Args:
            client (Flask test client): The Flask test client object.
        """
        response = client.get('/')
        assert response.status_code == 200
        assert b'<h1 id="gpatitle" class="text-[3vw] font-[800]">Welcome to the <span id="calctitle">GPA Calculator</span></h1>' in response.data

    def test_add_grade_route(self, client):
        """
        Test case to ensure the add_grade route renders correctly.

        Args:
            client (Flask test client): The Flask test client object.
        """
        response = client.get('/add_grade')
        assert response.status_code == 200
        assert b'<label for="course_name">Course Name:</label>' in response.data

    def test_add_grade_post(self, client, mock_mongodb):
        form_data = {
            "course_name": "Software Engineering",
            "course_grade": "A",
            "course_credits": "4",
            "semester": "Spring 2024",
            "instructor": "T. Tester"
        }
        response = client.post("/add_grade", data=form_data)
        
        assert response.status_code == 302
        
        mock_mongodb.insert_one.assert_called_once()
        # Check that the data passed to the database is correct
        args, kwargs = mock_mongodb.insert_one.call_args
        assert args[0] == {
            "course_name": "Software Engineering",
            "course_grade": "A",
            "course_credits": "4",
            "semester": "Spring 2024",
            "instructor": "T. Tester"
        }

    def test_calculate_route(self, client):
        """
        Test case to ensure the calculate route renders correctly.

        Args:
            client (Flask test client): The Flask test client object.
        """
        response = client.get('/calculate')
        assert response.status_code == 200
        assert b'<label for="current_grade">Current grade:</label>' in response.data

    def test_calculate_route_post(self, client):
        """
        Test case to ensure the calculate route post works correctly.

        Args:
            client (Flask
             test client): The Flask test client object.
        """
        response = client.post('/calculate', data='{"current_grade": "80", "target_grade": "90", "final_weight": "30"}')
        assert response.status_code == 200