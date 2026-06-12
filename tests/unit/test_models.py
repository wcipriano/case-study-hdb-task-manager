from project.todo.models import User, Task


def test_new_user():
    user = User(username="joe", password="123")
    assert user.username == 'joe'
    # assert user.password_hashed != 'FlaskIsAwesome'
    assert user.__repr__() == "User('joe')"


def test_new_user_with_fixture(new_user):
    assert new_user.username == 'joe'
    assert new_user.password == '123'

def test_user_id(new_user):
    new_user.id = 17
    assert isinstance(new_user.get_id(), str)
    assert not isinstance(new_user.get_id(), int)
    assert new_user.get_id() == '17'


def test_new_task():
    task = Task(id=6, content='Task1', date_posted='2026-06-11', user_id=1)
    assert task.id == 6
    assert task.content == 'Task1'
    assert task.date_posted == '2026-06-11'
    assert task.user_id == 1
    assert task.__repr__() == f"Task('Task1', '2026-06-11', '1')"
