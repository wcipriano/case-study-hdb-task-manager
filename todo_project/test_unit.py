import pytest
from todo_app import create_app, get_db
from todo_app.models import User


# @pytest.fixture(autouse=True, scope="class")
@pytest.fixture(scope="class")
def app():
    # config = dict(SQLALCHEMY_DATABASE_URI="sqlite:///site.db", TESTING=True, SQLALCHEMY_TRACK_MODIFICATIONS=False)
    config = dict(SQLALCHEMY_DATABASE_URI="sqlite:///:memory:", TESTING=True, SQLALCHEMY_TRACK_MODIFICATIONS=False)
    app = create_app(config)
    yield app  # Provide the app instance to tests


@pytest.fixture(scope="class")
def db(app):
    with app.app_context():
        db = get_db(app)
        db.create_all()  # Create all tables defined in your models
        yield db  # Provide the app instance to tests
        # db.drop_all()  # Clean up and destroy tables after the test completes


class TestUser:
    """Unit test ensuring state of the database."""

    @staticmethod
    def get_user(username, app, db):
        """Unit test ensuring state of the database."""
        with app.app_context():
            s = db.select(User).filter_by(username=username)
            user = db.session.execute(s).scalar_one_or_none()
            return user

    @staticmethod
    def test_user_not_found(app, db):
        """Unit test ensuring state of the database."""
        user = TestUser.get_user("joe", app, db)
        assert user is None, "User joe should not exist in database"

    @staticmethod
    def test_user_delete(app, db):
        """Unit test ensuring data remove."""
        # Given: a valid user object
        user = TestUser.get_user("alice", app, db)
        if user:
            # When: delete and committed to the database
            with app.app_context():
                db.session.delete(user)
                db.session.commit()
        # Then: assert data values are exact
        user = TestUser.get_user("alice", app, db)
        assert user is None, "User alice should not exist in database after deleting"

    @staticmethod
    def test_user_create(app, db):
        """Unit test ensuring data correctly persists inside the database."""
        # Given: a valid user object
        user = TestUser.get_user("alice", app, db)
        if not user:
            # Given: a valid user object
            user = User(username="alice", password="test1")

            # When: added and committed to the database
            with app.app_context():
                db.session.add(user)
                db.session.commit()
                print(user)

        # Then: assert data values are exact
        assert user.id is not None
        assert user.username == "alice"
