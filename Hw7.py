# 1

persons = [
    ('Kelly', 'Simpson', 26),
    ('Erika', 'Stephens', 24),
    ('Cheryl', 'Dunn', 30),
    ('Amy', 'Larsen', 49),
    ('Christine', 'Gordon', 23),
    ('Monica', 'Huff', 38),
    ('David', 'Nixon', 36),
    ('Cindy', 'Escobar', 41),
    ('Cindy', 'White', 33),
    ('Joel', 'Hall', 43),
    ('Steven', 'Winters', 28),
    ('Alex', 'Cole', 68),
    ('Alex', 'Smith', 32),
    ('Brittany', 'Thompson', 18),
    ('Ernest', 'Young', 43),
    ('Traci', 'Wells', 38),
    ('Andrew', 'Flores', 61),
    ('Christopher', 'Lewis', 29),
    ('Kevin', 'Willis', 57),
    ('Kayla', 'Lucas', 28),
    ('Michelle', 'Rush', 43),
    ('Thomas', 'Mason', 37)
]

while True:
    name = input("შეიყვანეთ სახელი: ")

    if name == "stop":
        break

    found_name = False

    for person in persons:
        if person[0] == name:
            found_name = True
            break

    if not found_name:
        print("სახელი ვერ ინახა სიაში")
        continue

    surname = input("შეიყვანეთ გვარი: ")

    if surname == "stop":
        break

    found_person = False

    for person in persons:
        if person[0] == name and person[1] == surname:
            print("ასაკი:", person[2])
            found_person = True
            break

    if not found_person:
        print("გვარი არ არის სიაში")


# 2

word1 = input("შეიყვანეთ პირველი სიტყვა: ")
word2 = input("შეიყვანეთ მეორე სიტყვა: ")

set1 = set(word1)
set2 = set(word2)

common = set1 & set2
different = set1 ^ set2
union = set1 | set2

print("ერთნაირი სიმბოლოები:", common)
print("განსხვავებული სიმბოლოები:", different)
print("გაერთიანებული სიმბოლოები:", union)
