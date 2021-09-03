from model.entities import Person, User, Compound
from serializer import to_json, from_json


def test_serialize():
    person = Person("Joe", "Doe")
    user = User("jdoe@domain.com", "P422w0RD")
    compound = Compound(person, user)
    print(to_json(compound))


def test_deserialize():
    compound = from_json("""\
    {
        "person": {
            "first_name": "Joe",
            "last_name": "Doe",
            "__type__": "model.entities.Person"
        },
        "user": {
            "email": "jdoe@domain.com",
            "password": null,
            "__type__": "model.entities.User"
        },
        "__type__": "model.entities.Compound"
    }""")
    print(compound)
    print(compound.user)
    print(compound.person.first_name)


if __name__ == '__main__':
    test_serialize()
    test_deserialize()
