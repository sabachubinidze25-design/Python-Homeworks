# TASK 1

squares_dict = {}

for i in range(1, 11):
    squares_dict[i] = i * i

print("Task 1 (loop):")
print(squares_dict)

squares_dict2 = {i: i * i for i in range(1, 11)}

print("Task 1 (dict comprehension):")
print(squares_dict2)
print()


# TASK 2

products = [
    {"cola": {
        "price": 1.5,
        "quantity": 10
    }},
    {"fanta": {
        "price": 2.5,
        "quantity": 5
    }},
    {"snickers": {
        "price": 3.5,
        "quantity": 12
    }},
    {"water": {
        "price": 4.5,
        "quantity": 8
    }},
    {"beer": {
        "price": 6.5,
        "quantity": 5
    }}
]


print("Task 2a - Product names:")
for product in products:
    for name in product:
        print(name)

print()

print("Task 2b - Total value:")
total = 0

for product in products:
    for name in product:
        price = product[name]["price"]
        quantity = product[name]["quantity"]
        total = total + (price * quantity)

print("Total:", total)
print()


# TASK 3

fruit_dict = {}

print("Task 3:")

while True:
    fruit = input("Enter your favorite fruit: ")

    if fruit == "stop":
        break

    if fruit in fruit_dict:
        fruit_dict[fruit] = fruit_dict[fruit] + 1
    else:
        fruit_dict[fruit] = 1

print(fruit_dict)
