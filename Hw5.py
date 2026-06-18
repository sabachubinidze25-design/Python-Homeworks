# TASK 1

import random
my_list = [10, 20, 30, 40, 50, 60]

total = 0
for num in my_list:
    total = total + num

average = total / 6

print("Task 1:")
print("List:", my_list)
print("Sum:", total)
print("Average:", average)
print()


# TASK 2

given_list = ['a', 'b', 2, 4, 2, 'c', 'j', 1, 'b', 'd', 'c', 4, 1]
unique_list = []

for item in given_list:
    if item not in unique_list:
        unique_list.append(item)

print("Task 2:")
print("Original list:", given_list)
print("Unique list:", unique_list)
print()


# TASK 3


random_list = [random.randint(-50, 50) for i in range(20)]
even_list = [num for num in random_list if num % 2 == 0]

print("Task 3:")
print("Random list (20 numbers):", random_list)
print("Even numbers only:", even_list)
print()


# TASK 4

long_names = []
short_names = []

print("Task 4:")
print("Enter names (type stop / exit / quit to finish):")

while True:
    name = input("Enter name: ")

    if name == "stop" or name == "Stop" or name == "exit" or name == "Exit" or name == "quit" or name == "Quit":
        break

    name = name.strip()
    name = name.capitalize()

    if len(name) > 3:
        long_names.append(name)
    else:
        short_names.append(name)

print()
print("Long names:", long_names)
print("Short names:", short_names)
