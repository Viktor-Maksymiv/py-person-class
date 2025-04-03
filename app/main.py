class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    person_list = []

    for person in people:
        person_obj = Person(person["name"], person["age"])
        if (person.get("wife") is not None
                and person["wife"] in Person.people.keys()):
            Person.people[person["wife"]].husband = person_obj
            person_obj.wife = Person.people[person["wife"]]
        elif (person.get("husband") is not None
              and person["husband"] in Person.people.keys()):
            Person.people[person["husband"]].wife = person_obj
            person_obj.husband = Person.people[person["husband"]]
        person_list.append(person_obj)
    return person_list
