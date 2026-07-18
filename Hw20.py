import json


def add_persons(count):
    # Read data from JSON file
    with open("persons.json", "r", encoding="utf-8") as file:
        persons = json.load(file)

    if len(persons) == 0:
        last_id = 0
    else:
        last_id = persons[-1]["id"]

    for _ in range(count):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))

        new_person = {
            "id": last_id + 1,
            "name": name,
            "age": age
        }

        persons.append(new_person)
        last_id += 1

    with open("persons.json", "w", encoding="utf-8") as file:
        json.dump(persons, file, indent=4)


add_persons(2)
