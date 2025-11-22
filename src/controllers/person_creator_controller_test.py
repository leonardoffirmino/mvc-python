import pytest
from .person_creator_controller import PersonCreatorController

class MockPeopleRepository:
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        pass

def teste_create():
    person_info = {
        "first_name": "JohnTest",
        "last_name": "DoeTest",
        "age": 23,
        "pet_id": 123
    }

    controller = PersonCreatorController(MockPeopleRepository())
    response = controller.create(person_info)

    assert response["data"]["type"] == "Person"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == person_info

def teste_create_error():
    person_info = {
        "first_name": "John 112",
        "last_name": "Doe Test",
        "age": 23,
        "pet_id": 123
    }

    controller = PersonCreatorController(MockPeopleRepository())
    with pytest.raises(Exception):
        controller.create(person_info)
