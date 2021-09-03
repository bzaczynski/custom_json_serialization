# JSON Serialization of Custom Classes in Python

Here's a quick and dirty hack allowing for serializing custom Python classes to JSON and the other way around.

**Note:** This code wasn't tested and contains plenty of corner cases that won't work as expected without spending some time fixing those issues.   

## Serialize

```python
from model.entities import Person, User, Compound
from serializer import to_json
person = Person("Joe", "Doe")
user = User("jdoe@domain.com", "P422w0RD")
compound = Compound(person, user)
print(to_json(compound))
```

The code above will output the following JSON string:

```json
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
}
```

## Deserialize

```python
from serializer import from_json
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
```

The corresponding output:

```
<model.entities.Compound object at 0x7f7a66359190>
User(email='jdoe@domain.com', password=None)
Joe
```
