from typing import NamedTuple


class Person:
    """A type with the .__dict__ attribute"""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class User(NamedTuple):
    """A type without .__dict__, but with a custom .__json__() method"""
    email: str
    password: str

    def __json__(self):
        return {"email": self.email, "password": None}


class Compound:
    """A compound type composed of other custom types."""
    def __init__(self, person, user):
        self.person = person
        self.user = user
