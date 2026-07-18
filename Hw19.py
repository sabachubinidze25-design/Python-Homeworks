class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: ({self.name}, {self.age})"


def serialize(person):
    return f"Name: {person.name}, Age: {person.age}"


def write_to_file(person, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(serialize(person))


def read_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.readline().strip()


def deserialize(data):
    parts = data.split(", ")
    name = parts[0].split(": ")[1]
    age = int(parts[1].split(": ")[1])
    return Person(name, age)


# Example

p1 = Person("Otar", 35)

write_to_file(p1, "person.txt")

data = read_from_file("person.txt")
print("Read from file:", data)

p2 = deserialize(data)

print("Deserialized object:")
print(p2)
