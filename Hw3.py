# Task 1

number = int(input("შეიყვანეთ რიცხვი: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"{number}-ის ფაქტორიალი არის: {factorial}")

# Task 2

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}")

# Task 3

price = 50
valid_money = [5, 10, 20]

insert = 0

while insert < price:
    money = int(input(f"შეიტანეთ კუპიურა (5,10,20): "))
    if money not in valid_money:
        print("არასწორი კუპიუტა, თავიდან სცადეთ")
        continue
    insert += money
    remaining = price - insert
    if remaining > 0:
        print(f"კიდევ უნდა შეიტანოთ {remaining} ლარი")

change = insert - price
print(f"გადასახადი მიღებულია")
if change > 0:
    print(f"ხურდა {change} ლარი")
