import os
import pytest

from project import create_app, db
from project.todo.models import Task, User


@pytest.fixture(scope='module')
def new_user():
    user = User(username="joe", password="123")
    return user


@pytest.fixture(scope='module')
def test_client():
    # Set the Testing configuration prior to creating the Flask application
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!


@pytest.fixture(scope='module')
def init_database(test_client):
    # Create the database and the database table
    db.create_all()

    # Insert user data
    default_user = User(username="jose", password="123")
    second_user = User(username="maria", password="123")
    db.session.add(default_user)
    db.session.add(second_user)

    # Commit the changes for the users
    db.session.commit()

    # Insert data
    task1 = Task('Task1', default_user.id)
    task2 = Task('Task2', default_user.id)
    task3 = Task('Task3', default_user.id)
    db.session.add(task1)
    db.session.add(task2)
    db.session.add(task3)

    # Commit the changes
    db.session.commit()

    yield  # this is where the testing happens!

    db.drop_all()


@pytest.fixture(scope='function')
def log_in_default_user(test_client):
    test_client.post('/login', data={'usarname': 'jose', 'password': '123'})

    yield  # this is where the testing happens!

    test_client.get('/logout')


@pytest.fixture(scope='function')
def log_in_second_user(test_client):
    test_client.post('/login',
                     data={'email': 'maria','password': '123'})

    yield   # this is where the testing happens!

    # Log out the user
    test_client.get('/logout')


@pytest.fixture(scope='module')
def cli_test_client():
    # Set the Testing configuration prior to creating the Flask application
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    runner = flask_app.test_cli_runner()

    yield runner  # this is where the testing happens!
