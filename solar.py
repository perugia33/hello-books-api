
# CREATE APP
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


# def create_app(test_config=None):
#     app = Flask(__name__)

#     if not test_config:
#         app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#         app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
#             "SQLALCHEMY_DATABASE_URI")
        
#     else:
#         app.config["TESTING"] = True
#         app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#         app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
#             "SQLALCHEMY_TEST_DATABASE_URI")

#     # Import models here
#     from app.models.planet import Planet

#     db.init_app(app)
#     migrate.init_app(app, db)

#     # Register Blueprints here
#     from .routes import books_bp
#     app.register_blueprint(books_bp)

#     return app

# tests/conftest.py
# import pytest
# from app import create_app
# from app import db
# from flask.signals import request_finished
# from app.models.book import Book

# @pytest.fixture
# def app():
    # app = create_app({"TESTING": True})

    # @request_finished.connect_via(app)
    # def expire_session(sender, response, **extra):
    #     db.session.remove()

    # with app.app_context():
    #     db.create_all()
    #     yield app

    # with app.app_context():
#         db.drop_all()

# @pytest.fixture
# def client(app):
#     return app.test_client()


# # Creates one planet

# @pytest.fixture
# def one_saved_planet(app):
#     # Arrange
#     pluto_planet = Planet(name="Pluto",
#                       description="Pluto was discovered in Feb 1930 by the Lowell Observatory", moons=0)
   
#     db.session.add(pluto_planet)
#     db.session.commit()

    # dont use
                # db.session.add_all([ocean_book, mountain_book])
                # # Alternatively, we could do
                # db.session.add(ocean_book)
                # db.session.add(mountain_book)
            
# test to get all planets with empty lis

def test_get_all_books_with_no_records(client):

    # Act
    response = client.get("/books")
    # This sends an HTTP request to /books. It returns
    #  an HTTP response object, which we store in our 
    # local variable response

    response_body = response.get_json()
    # the JSON response body with response.get_json()

     # Assert
    assert response.status_code == 200
    # read that status code and check it 
    # against the expected status code
