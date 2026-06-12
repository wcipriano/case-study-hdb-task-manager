"""
This file (test_app.py) contains the unit tests for the Flask application.
"""
import pytest
from pydantic import ValidationError

from project.todo.models import Task


def test_validate_user_data_nominal():
    task = Task(content='task11', user_id=1)
    assert task.content == 'task11'


# def test_validate_user_data_missing_inputs():
#     with pytest.raises(ValidationError):
#         Task()  # Missing input data!

